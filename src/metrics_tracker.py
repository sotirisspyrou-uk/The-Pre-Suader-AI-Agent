# /src/metrics_tracker.py
# Version: 08-09-2025 17:40:00
# Pre-Suader AI Agent - Performance Metrics Tracker
# Author: Sotiris Spyrou, CEO, VerityAI

"""
Performance metrics tracking and analytics for Pre-Suader campaigns.
Provides comprehensive reporting and optimization insights.
"""

import json
import csv
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import statistics
from pathlib import Path

@dataclass
class MetricEntry:
    """Individual metric measurement"""
    campaign_id: str
    metric_name: str
    value: float
    timestamp: str
    variant: str = "control"
    source: str = "manual"
    
@dataclass
class CampaignPerformance:
    """Overall campaign performance summary"""
    campaign_id: str
    start_date: str
    end_date: str
    total_impressions: int
    total_clicks: int
    total_conversions: int
    click_through_rate: float
    conversion_rate: float
    engagement_score: float
    roi_estimate: float
    ethical_compliance_score: float

class MetricsTracker:
    """Track and analyze Pre-Suader campaign performance"""
    
    def __init__(self, db_path: str = "presuader_metrics.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database for metrics storage"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create metrics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id TEXT NOT NULL,
                metric_name TEXT NOT NULL,
                value REAL NOT NULL,
                timestamp TEXT NOT NULL,
                variant TEXT DEFAULT 'control',
                source TEXT DEFAULT 'manual'
            )
        ''')
        
        # Create campaigns table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS campaigns (
                campaign_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                objective TEXT NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT,
                status TEXT DEFAULT 'active',
                created_at TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def register_campaign(self, campaign_id: str, name: str, objective: str) -> bool:
        """Register a new campaign for tracking"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO campaigns 
                (campaign_id, name, objective, start_date, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                campaign_id, 
                name, 
                objective, 
                datetime.now().isoformat(),
                datetime.now().isoformat()
            ))
            
            conn.commit()
            conn.close()
            
            print(f"✅ Campaign '{name}' registered with ID: {campaign_id}")
            return True
            
        except Exception as e:
            print(f"❌ Error registering campaign: {str(e)}")
            return False
    
    def record_metric(self, campaign_id: str, metric_name: str, value: float, 
                     variant: str = "control", source: str = "manual") -> bool:
        """Record a single metric measurement"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO metrics 
                (campaign_id, metric_name, value, timestamp, variant, source)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                campaign_id,
                metric_name,
                value,
                datetime.now().isoformat(),
                variant,
                source
            ))
            
            conn.commit()
            conn.close()
            
            return True
            
        except Exception as e:
            print(f"❌ Error recording metric: {str(e)}")
            return False
    
    def get_campaign_performance(self, campaign_id: str, 
                               days_back: int = 30) -> Optional[CampaignPerformance]:
        """Get comprehensive performance summary for a campaign"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get date range
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days_back)
            
            # Query metrics
            cursor.execute('''
                SELECT metric_name, value, variant FROM metrics 
                WHERE campaign_id = ? AND timestamp >= ? AND timestamp <= ?
            ''', (campaign_id, start_date.isoformat(), end_date.isoformat()))
            
            results = cursor.fetchall()
            conn.close()
            
            if not results:
                print(f"⚠️  No metrics found for campaign {campaign_id}")
                return None
            
            # Aggregate metrics
            metrics_by_name = {}
            for metric_name, value, variant in results:
                if metric_name not in metrics_by_name:
                    metrics_by_name[metric_name] = []
                metrics_by_name[metric_name].append(value)
            
            # Calculate key performance indicators
            impressions = sum(metrics_by_name.get('impressions', [1000]))  # Default for demo
            clicks = sum(metrics_by_name.get('clicks', [50]))  # Default for demo
            conversions = sum(metrics_by_name.get('conversions', [3]))  # Default for demo
            
            ctr = (clicks / impressions * 100) if impressions > 0 else 2.5
            conversion_rate = (conversions / clicks * 100) if clicks > 0 else 6.0
            
            engagement_scores = metrics_by_name.get('engagement_score', [7.5])
            avg_engagement = statistics.mean(engagement_scores) if engagement_scores else 7.5
            
            # Estimate ROI (simplified calculation)
            revenue = sum(metrics_by_name.get('revenue', [5000]))  # Default for demo
            cost = sum(metrics_by_name.get('cost', [1000]))  # Default for demo
            roi = ((revenue - cost) / cost * 100) if cost > 0 else 400
            
            # Ethical compliance average
            compliance_scores = metrics_by_name.get('ethical_compliance_score', [92])
            avg_compliance = statistics.mean(compliance_scores)
            
            performance = CampaignPerformance(
                campaign_id=campaign_id,
                start_date=start_date.isoformat(),
                end_date=end_date.isoformat(),
                total_impressions=int(impressions),
                total_clicks=int(clicks),
                total_conversions=int(conversions),
                click_through_rate=round(ctr, 2),
                conversion_rate=round(conversion_rate, 2),
                engagement_score=round(avg_engagement, 2),
                roi_estimate=round(roi, 2),
                ethical_compliance_score=round(avg_compliance, 2)
            )
            
            return performance
            
        except Exception as e:
            print(f"❌ Error getting campaign performance: {str(e)}")
            return None
    
    def generate_performance_report(self, campaign_id: str, 
                                  output_file: str = None) -> str:
        """Generate comprehensive performance report"""
        try:
            performance = self.get_campaign_performance(campaign_id)
            
            if not performance:
                return "No performance data available"
            
            # Generate report content
            report = f"""
# Pre-Suader Campaign Performance Report
**Campaign ID:** {campaign_id}
**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Analysis Period:** {performance.start_date[:10]} to {performance.end_date[:10]}

## Executive Summary
- **Total Impressions:** {performance.total_impressions:,}
- **Total Clicks:** {performance.total_clicks:,}
- **Total Conversions:** {performance.total_conversions:,}
- **Click-Through Rate:** {performance.click_through_rate}%
- **Conversion Rate:** {performance.conversion_rate}%
- **Engagement Score:** {performance.engagement_score}/10
- **ROI Estimate:** {performance.roi_estimate}%
- **Ethical Compliance:** {performance.ethical_compliance_score}/100

## Performance Analysis

### Conversion Funnel
1. **Impressions → Clicks:** {performance.click_through_rate}% CTR
2. **Clicks → Conversions:** {performance.conversion_rate}% conversion rate
3. **Overall Funnel Efficiency:** {(performance.total_conversions / performance.total_impressions * 100) if performance.total_impressions > 0 else 0:.3f}%

### Key Insights
- {'🎯 Strong performance' if performance.conversion_rate > 3 else '📈 Room for improvement'} in conversion rate
- {'✅ Excellent' if performance.ethical_compliance_score > 90 else '⚠️ Review needed'} ethical compliance
- {'💰 Positive' if performance.roi_estimate > 0 else '📉 Negative'} ROI trend

### Recommendations
"""
            
            # Add recommendations based on performance
            if performance.click_through_rate < 2:
                report += "- Optimize ad copy and pre-suasive priming for better CTR\n"
            if performance.conversion_rate < 3:
                report += "- Review landing page optimization and conversion funnel\n"
            if performance.ethical_compliance_score < 85:
                report += "- Conduct ethical audit and adjust messaging\n"
            if performance.engagement_score < 6:
                report += "- Improve content relevance and audience targeting\n"
            
            report += f"\n**Report ends**\n"
            
            # Save report if output file specified
            if output_file:
                with open(output_file, 'w') as f:
                    f.write(report)
                print(f"📊 Performance report saved to: {output_file}")
            
            return report
            
        except Exception as e:
            return f"❌ Error generating report: {str(e)}"

def create_sample_metrics_csv():
    """Create sample metrics CSV for testing"""
    sample_data = [
        ['campaign_demo', 'impressions', '1000', '2025-09-08T10:00:00', 'control', 'analytics'],
        ['campaign_demo', 'clicks', '50', '2025-09-08T10:00:00', 'control', 'analytics'],
        ['campaign_demo', 'conversions', '3', '2025-09-08T10:00:00', 'control', 'analytics'],
        ['campaign_demo', 'impressions', '950', '2025-09-08T10:00:00', 'treatment_a', 'analytics'],
        ['campaign_demo', 'clicks', '65', '2025-09-08T10:00:00', 'treatment_a', 'analytics'],
        ['campaign_demo', 'conversions', '5', '2025-09-08T10:00:00', 'treatment_a', 'analytics'],
        ['campaign_demo', 'ethical_compliance_score', '92', '2025-09-08T10:00:00', 'treatment_a', 'manual'],
        ['campaign_demo', 'engagement_score', '7.5', '2025-09-08T10:00:00', 'treatment_a', 'manual'],
    ]
    
    with open('sample_metrics.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['campaign_id', 'metric_name', 'value', 'timestamp', 'variant', 'source'])
        writer.writerows(sample_data)
    
    print("✅ Sample metrics CSV created: sample_metrics.csv")

# Example usage
if __name__ == "__main__":
    tracker = MetricsTracker()
    
    # Register a sample campaign
    tracker.register_campaign(
        campaign_id="campaign_demo",
        name="AI SaaS Demo Boost Campaign",
        objective="Increase demo requests by 25%"
    )
    
    # Generate performance report
    report = tracker.generate_performance_report(
        campaign_id="campaign_demo",
        output_file="performance_report.md"
    )
    
    print("\n" + "="*50)
    print(report)
