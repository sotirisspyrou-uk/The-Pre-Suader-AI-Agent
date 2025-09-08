# /src/presuader_core_functions.py
# Version: 08-09-2025 17:40:00
# Pre-Suader AI Agent - Core Functions
# Author: Sotiris Spyrou, CEO, VerityAI

"""
Core Pre-Suader AI Agent functionality for ethical marketing optimization.
Implements Robert Cialdini's Pre-Suasion principles for AI SaaS campaigns.
"""

import json
import csv
import re
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
import hashlib

@dataclass
class AudienceProfile:
    """Data structure for target audience psychological profile"""
    segment_name: str
    demographics: Dict[str, str]
    psychological_triggers: List[str]
    values: List[str]
    pain_points: List[str]
    preferred_channels: List[str]
    decision_factors: List[str]
    trust_indicators: List[str]

@dataclass
class PreSuasiveStrategy:
    """Data structure for pre-suasive campaign strategy"""
    campaign_id: str
    objective: str
    target_audience: AudienceProfile
    priming_sequence: List[Dict[str, str]]
    success_metrics: Dict[str, float]
    ethical_guidelines: List[str]
    implementation_timeline: List[Dict[str, str]]

class PreSuaderCore:
    """Core Pre-Suader AI Agent Functions"""
    
    def __init__(self):
        self.ethical_keywords = [
            'manipulate', 'deceive', 'trick', 'exploit', 'coerce', 
            'mislead', 'dark pattern', 'false scarcity', 'fake urgency'
        ]
        self.positive_triggers = [
            'trust', 'innovation', 'efficiency', 'growth', 'success',
            'reliability', 'expertise', 'transparency', 'value', 'results'
        ]
    
    def analyze_audience_psychology(self, audience_data: Dict) -> AudienceProfile:
        """
        Analyze target audience psychological triggers and create profile
        
        Args:
            audience_data: Dictionary containing audience demographics, behaviors, preferences
            
        Returns:
            AudienceProfile: Structured psychological profile for pre-suasion targeting
        """
        # Extract psychological triggers based on behavior patterns
        triggers = []
        if audience_data.get('tech_savvy', False):
            triggers.extend(['innovation', 'efficiency', 'cutting-edge'])
        if audience_data.get('business_focused', False):
            triggers.extend(['ROI', 'productivity', 'competitive advantage'])
        if audience_data.get('risk_averse', False):
            triggers.extend(['security', 'reliability', 'proven results'])
            
        # Identify core values from stated preferences
        values = []
        if 'transparency' in str(audience_data.get('preferences', '')).lower():
            values.append('transparency')
        if 'innovation' in str(audience_data.get('interests', '')).lower():
            values.append('innovation')
        if 'quality' in str(audience_data.get('priorities', '')).lower():
            values.append('quality')
            
        # Create structured profile
        profile = AudienceProfile(
            segment_name=audience_data.get('segment_name', 'Primary Segment'),
            demographics=audience_data.get('demographics', {}),
            psychological_triggers=triggers,
            values=values,
            pain_points=audience_data.get('pain_points', []),
            preferred_channels=audience_data.get('channels', ['email', 'web']),
            decision_factors=audience_data.get('decision_factors', ['price', 'features']),
            trust_indicators=audience_data.get('trust_indicators', ['testimonials', 'case studies'])
        )
        
        return profile
    
    def generate_presuasive_strategy(self, audience_profile: AudienceProfile, 
                                   campaign_objective: str) -> PreSuasiveStrategy:
        """
        Generate comprehensive pre-suasive strategy based on audience psychology
        
        Args:
            audience_profile: Analyzed audience psychological profile
            campaign_objective: Specific campaign goal (e.g., "increase demo requests")
            
        Returns:
            PreSuasiveStrategy: Complete strategy with priming sequences and metrics
        """
        # Generate campaign ID
        campaign_id = hashlib.md5(
            f"{audience_profile.segment_name}{campaign_objective}{datetime.now()}".encode()
        ).hexdigest()[:8]
        
        # Design priming sequence based on psychological triggers
        priming_sequence = [
            {
                "stage": "attention_direction",
                "technique": "value_alignment",
                "content": f"Prime with {', '.join(audience_profile.values[:2])} messaging",
                "timing": "first_touchpoint"
            },
            {
                "stage": "association_building",
                "technique": "trigger_activation",
                "content": f"Associate brand with {audience_profile.psychological_triggers[0] if audience_profile.psychological_triggers else 'innovation'}",
                "timing": "pre_main_message"
            },
            {
                "stage": "trust_establishment",
                "technique": "social_proof",
                "content": f"Display {', '.join(audience_profile.trust_indicators)}",
                "timing": "validation_moment"
            }
        ]
        
        # Set success metrics
        success_metrics = {
            "click_through_rate_lift": 25.0,
            "session_duration_lift": 40.0,
            "conversion_rate_lift": 20.0,
            "engagement_score_target": 8.0
        }
        
        # Define ethical guidelines
        ethical_guidelines = [
            "Prioritize genuine user benefit over conversion metrics",
            "Maintain transparency in all communications",
            "Respect user autonomy and decision-making",
            "Avoid exploiting psychological vulnerabilities",
            "Provide clear value proposition without deception"
        ]
        
        # Create implementation timeline
        timeline = [
            {"week": "1", "task": "Audience analysis and strategy finalization"},
            {"week": "2", "task": "Content creation and pre-suasive optimization"},
            {"week": "3", "task": "A/B testing setup and initial deployment"},
            {"week": "4", "task": "Performance monitoring and optimization"}
        ]
        
        strategy = PreSuasiveStrategy(
            campaign_id=campaign_id,
            objective=campaign_objective,
            target_audience=audience_profile,
            priming_sequence=priming_sequence,
            success_metrics=success_metrics,
            ethical_guidelines=ethical_guidelines,
            implementation_timeline=timeline
        )
        
        return strategy
    
    def optimize_content_for_presuasion(self, original_content: str, 
                                       strategy: PreSuasiveStrategy) -> Dict[str, str]:
        """
        Optimize marketing content with pre-suasive elements
        
        Args:
            original_content: Original marketing copy or content
            strategy: Pre-suasive strategy to apply
            
        Returns:
            Dict: Original and optimized content versions with A/B variants
        """
        if not strategy:
            # Fallback optimization without strategy
            optimized_content = f"🚀 Revolutionary Technology\n\n{original_content}\n\n✅ Trusted by 1000+ businesses worldwide"
        else:
            audience = strategy.target_audience
            # Apply pre-suasive optimization
            optimized_content = self._apply_presuasive_optimization(
                original_content, audience.psychological_triggers, audience.values
            )
        
        # Create A/B testing variants
        variant_a = original_content.replace("our", "proven").replace("new", "trusted")
        variant_b = f"⭐ Advanced Solution\n\n{original_content}"
        variant_c = f"⚡ BREAKTHROUGH: {original_content}\n\n🎯 Limited Early Access Available"
        
        return {
            "original": original_content,
            "optimized": optimized_content,
            "variant_a_conservative": variant_a,
            "variant_b_moderate": variant_b,
            "variant_c_aggressive": variant_c,
            "optimization_notes": "Pre-suasive optimization applied with attention direction and trust indicators"
        }
    
    def _apply_presuasive_optimization(self, content: str, triggers: List[str], 
                                     values: List[str]) -> str:
        """Apply pre-suasive optimization techniques to content"""
        optimized = content
        
        # Add attention-directing elements
        if 'innovation' in triggers:
            optimized = f"🚀 Revolutionary AI Technology\n\n{optimized}"
        
        # Incorporate value alignment
        for value in values[:2]:
            if value.lower() not in optimized.lower():
                optimized = optimized.replace(
                    "features", f"{value}-focused features", 1
                )
        
        # Add social proof elements
        if 'trust' in triggers or 'reliability' in triggers:
            optimized += "\n\n✅ Trusted by 1000+ businesses worldwide"
        
        return optimized
    
    def monitor_ethical_compliance(self, content: str, strategy: PreSuasiveStrategy = None) -> Dict[str, any]:
        """
        Monitor content for ethical compliance and potential manipulation
        
        Args:
            content: Content to analyze for ethical issues
            strategy: Strategy context for evaluation (optional)
            
        Returns:
            Dict: Compliance report with scores and recommendations
        """
        issues = []
        warnings = []
        score = 100.0
        
        # Check for manipulative language
        content_lower = content.lower()
        for keyword in self.ethical_keywords:
            if keyword in content_lower:
                issues.append(f"Potentially manipulative language detected: '{keyword}'")
                score -= 10.0
        
        # Check for false urgency
        urgency_patterns = [
            r'limited time', r'act now', r'hurry', r'expires', r'only \d+ left'
        ]
        for pattern in urgency_patterns:
            if re.search(pattern, content_lower):
                warnings.append(f"Urgency language detected: review for authenticity")
                score -= 5.0
        
        # Check transparency
        if not any(word in content_lower for word in ['transparent', 'honest', 'clear']):
            warnings.append("Consider adding transparency indicators")
            score -= 3.0
        
        # Generate compliance grade
        if score >= 90:
            grade = "A - Excellent ethical compliance"
        elif score >= 80:
            grade = "B - Good compliance with minor improvements needed"
        elif score >= 70:
            grade = "C - Acceptable but requires attention"
        else:
            grade = "D - Significant ethical concerns require addressing"
        
        return {
            "compliance_score": max(0, score),
            "grade": grade,
            "issues": issues,
            "warnings": warnings,
            "recommendations": self._generate_ethical_recommendations(issues, warnings),
            "audit_timestamp": datetime.now().isoformat()
        }
    
    def _generate_ethical_recommendations(self, issues: List[str], warnings: List[str]) -> List[str]:
        """Generate specific recommendations for ethical improvements"""
        recommendations = []
        
        if issues:
            recommendations.append("Remove or replace manipulative language with value-focused messaging")
            recommendations.append("Ensure all claims are truthful and verifiable")
        
        if warnings:
            recommendations.append("Add transparency statements about product capabilities")
            recommendations.append("Include clear opt-out mechanisms for all communications")
            recommendations.append("Verify urgency claims are based on genuine limitations")
        
        recommendations.append("Conduct user testing to verify message clarity and honesty")
        recommendations.append("Review campaign against company ethical guidelines")
        
        return recommendations
    
    def save_strategy_report(self, strategy: PreSuasiveStrategy, 
                           output_path: str = "presuasive_strategy_report.json") -> str:
        """Save complete strategy report to file"""
        report = {
            "strategy": asdict(strategy),
            "generated_at": datetime.now().isoformat(),
            "version": "1.0",
            "author": "Pre-Suader AI Agent"
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return output_path

# Example usage function
def example_usage():
    """Example of how to use Pre-Suader core functions"""
    
    # Initialize Pre-Suader
    presuader = PreSuaderCore()
    
    # Sample audience data
    audience_data = {
        "segment_name": "Tech-Savvy Business Owners",
        "demographics": {"age_range": "35-50", "industry": "technology", "role": "decision_maker"},
        "tech_savvy": True,
        "business_focused": True,
        "pain_points": ["inefficient processes", "high costs", "competitive pressure"],
        "values": ["innovation", "transparency", "results"],
        "channels": ["email", "linkedin", "web"],
        "decision_factors": ["ROI", "ease_of_use", "support_quality"],
        "trust_indicators": ["case_studies", "testimonials", "free_trial"]
    }
    
    # Analyze audience psychology
    audience_profile = presuader.analyze_audience_psychology(audience_data)
    print(f"Audience Profile: {audience_profile.segment_name}")
    print(f"Key Triggers: {audience_profile.psychological_triggers}")
    
    # Generate pre-suasive strategy
    strategy = presuader.generate_presuasive_strategy(
        audience_profile, 
        "increase demo requests by 25%"
    )
    print(f"\nStrategy ID: {strategy.campaign_id}")
    print(f"Priming Stages: {len(strategy.priming_sequence)}")
    
    # Optimize sample content
    original_content = """
    Discover our AI productivity platform that helps businesses automate workflows and save time.
    Book a demo today to see how we can transform your operations.
    """
    
    optimized_content = presuader.optimize_content_for_presuasion(original_content, strategy)
    print(f"\nOriginal: {original_content}")
    print(f"Optimized: {optimized_content['optimized']}")
    
    # Check ethical compliance
    compliance = presuader.monitor_ethical_compliance(
        optimized_content['optimized'], 
        strategy
    )
    print(f"\nEthical Compliance: {compliance['grade']}")
    print(f"Score: {compliance['compliance_score']}/100")
    
    # Save strategy report
    report_path = presuader.save_strategy_report(strategy)
    print(f"\nStrategy saved to: {report_path}")

if __name__ == "__main__":
    example_usage()
