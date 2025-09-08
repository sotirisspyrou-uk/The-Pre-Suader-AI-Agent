# /src/presuader_cli.py
# Version: 08-09-2025 17:40:00
# Pre-Suader AI Agent - Command Line Interface
# Author: Sotiris Spyrou, CEO, VerityAI

"""
Command-line interface for Pre-Suader AI Agent.
Provides user-friendly access to all core functionality.
"""

import argparse
import json
import sys
from pathlib import Path
from presuader_core_functions import PreSuaderCore, AudienceProfile

class PreSuaderCLI:
    """Command-line interface for Pre-Suader AI Agent"""
    
    def __init__(self):
        self.presuader = PreSuaderCore()
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
    
    def analyze_audience(self, input_file: str) -> str:
        """Analyze audience from JSON file and create psychological profile"""
        try:
            with open(input_file, 'r') as f:
                audience_data = json.load(f)
            
            profile = self.presuader.analyze_audience_psychology(audience_data)
            
            output_file = self.output_dir / f"audience_profile_{profile.segment_name.replace(' ', '_').lower()}.json"
            with open(output_file, 'w') as f:
                json.dump(profile.__dict__, f, indent=2)
            
            print(f"✅ Audience analysis complete!")
            print(f"📊 Profile saved to: {output_file}")
            print(f"🎯 Key triggers: {', '.join(profile.psychological_triggers[:3])}")
            print(f"💎 Core values: {', '.join(profile.values[:3])}")
            
            return str(output_file)
            
        except FileNotFoundError:
            print(f"❌ Error: Input file '{input_file}' not found")
            return ""
        except json.JSONDecodeError:
            print(f"❌ Error: Invalid JSON format in '{input_file}'")
            return ""
    
    def create_strategy(self, profile_file: str, objective: str) -> str:
        """Create pre-suasive strategy from audience profile"""
        try:
            with open(profile_file, 'r') as f:
                profile_data = json.load(f)
            
            # Reconstruct AudienceProfile object
            profile = AudienceProfile(**profile_data)
            
            # Generate strategy
            strategy = self.presuader.generate_presuasive_strategy(profile, objective)
            
            output_file = self.output_dir / f"strategy_{strategy.campaign_id}.json"
            self.presuader.save_strategy_report(strategy, str(output_file))
            
            print(f"✅ Pre-suasive strategy created!")
            print(f"📋 Strategy ID: {strategy.campaign_id}")
            print(f"🎯 Objective: {objective}")
            print(f"⚡ Priming stages: {len(strategy.priming_sequence)}")
            print(f"📁 Strategy saved to: {output_file}")
            
            return str(output_file)
            
        except FileNotFoundError:
            print(f"❌ Error: Profile file '{profile_file}' not found")
            return ""
        except Exception as e:
            print(f"❌ Error creating strategy: {str(e)}")
            return ""
    
    def optimize_content(self, strategy_file: str, content_file: str) -> str:
        """Optimize marketing content using pre-suasive strategy"""
        try:
            # Load strategy
            with open(strategy_file, 'r') as f:
                strategy_data = json.load(f)
            
            # Load content
            with open(content_file, 'r') as f:
                original_content = f.read()
            
            # Optimize content (simplified for CLI)
            optimized = self.presuader.optimize_content_for_presuasion(original_content, None)
            
            # Save optimized versions
            base_name = Path(content_file).stem
            output_files = []
            
            for variant_name, content in optimized.items():
                if variant_name != "optimization_notes":
                    output_file = self.output_dir / f"{base_name}_{variant_name}.txt"
                    with open(output_file, 'w') as f:
                        f.write(content)
                    output_files.append(str(output_file))
            
            print(f"✅ Content optimization complete!")
            print(f"📝 Generated {len(output_files)} variants")
            print(f"📁 Files saved to: {self.output_dir}")
            
            return str(self.output_dir)
            
        except FileNotFoundError as e:
            print(f"❌ Error: File not found - {str(e)}")
            return ""
        except Exception as e:
            print(f"❌ Error optimizing content: {str(e)}")
            return ""
    
    def check_ethics(self, content_file: str, strategy_file: str = None) -> str:
        """Check content for ethical compliance"""
        try:
            with open(content_file, 'r') as f:
                content = f.read()
            
            compliance = self.presuader.monitor_ethical_compliance(content, None)
            
            # Save compliance report
            base_name = Path(content_file).stem
            report_file = self.output_dir / f"{base_name}_ethics_report.json"
            with open(report_file, 'w') as f:
                json.dump(compliance, f, indent=2)
            
            print(f"✅ Ethical compliance check complete!")
            print(f"🏆 Grade: {compliance['grade']}")
            print(f"📊 Score: {compliance['compliance_score']}/100")
            
            if compliance['issues']:
                print(f"⚠️  Issues found: {len(compliance['issues'])}")
                for issue in compliance['issues']:
                    print(f"   • {issue}")
            
            if compliance['warnings']:
                print(f"💡 Warnings: {len(compliance['warnings'])}")
                for warning in compliance['warnings'][:3]:  # Show first 3
                    print(f"   • {warning}")
            
            print(f"📁 Full report saved to: {report_file}")
            
            return str(report_file)
            
        except FileNotFoundError:
            print(f"❌ Error: Content file '{content_file}' not found")
            return ""
        except Exception as e:
            print(f"❌ Error checking ethics: {str(e)}")
            return ""
    
    def create_sample_files(self) -> None:
        """Create sample input files for testing"""
        sample_audience = {
            "segment_name": "Tech Startup Founders",
            "demographics": {
                "age_range": "28-45",
                "industry": "technology",
                "role": "founder/CEO"
            },
            "tech_savvy": True,
            "business_focused": True,
            "risk_averse": False,
            "pain_points": [
                "scaling challenges",
                "funding pressure",
                "competitive market",
                "team productivity"
            ],
            "values": ["innovation", "growth", "efficiency", "transparency"],
            "channels": ["email", "linkedin", "twitter", "web"],
            "decision_factors": ["ROI", "scalability", "ease_of_use", "support"],
            "trust_indicators": ["case_studies", "peer_recommendations", "free_trial"]
        }
        
        sample_content = """Transform Your Startup with AI-Powered Productivity
        
Our advanced AI platform helps growing companies automate repetitive tasks, streamline workflows, and scale operations efficiently. 

Join hundreds of successful startups who've increased their productivity by 40% while reducing operational costs.

Features:
• Intelligent task automation
• Real-time collaboration tools
• Advanced analytics dashboard
• 24/7 customer support

Ready to supercharge your growth? Book a free demo today and see how we can transform your operations.

Start your free 14-day trial - no credit card required."""
        
        # Create sample files
        audience_file = Path("sample_audience.json")
        content_file = Path("sample_content.txt")
        
        with open(audience_file, 'w') as f:
            json.dump(sample_audience, f, indent=2)
        
        with open(content_file, 'w') as f:
            f.write(sample_content)
        
        print(f"✅ Sample files created!")
        print(f"📁 {audience_file} - Sample audience data")
        print(f"📁 {content_file} - Sample marketing content")
        print(f"\n🚀 Quick start:")
        print(f"   python src/presuader_cli.py analyze {audience_file}")
        print(f"   python src/presuader_cli.py optimize-content strategy_*.json {content_file}")

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="Pre-Suader AI Agent - Ethical Pre-Suasion Marketing Optimization",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create sample files for testing
  python src/presuader_cli.py create-samples
  
  # Analyze audience psychology
  python src/presuader_cli.py analyze sample_audience.json
  
  # Create pre-suasive strategy
  python src/presuader_cli.py strategy output/audience_profile_*.json "increase demo requests"
  
  # Optimize marketing content
  python src/presuader_cli.py optimize-content output/strategy_*.json sample_content.txt
  
  # Check ethical compliance
  python src/presuader_cli.py check-ethics sample_content.txt
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Analyze audience command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze audience psychology')
    analyze_parser.add_argument('input_file', help='JSON file with audience data')
    
    # Strategy command
    strategy_parser = subparsers.add_parser('strategy', help='Create pre-suasive strategy')
    strategy_parser.add_argument('profile_file', help='Audience profile JSON file')
    strategy_parser.add_argument('objective', help='Campaign objective')
    
    # Optimize content command
    optimize_parser = subparsers.add_parser('optimize-content', help='Optimize marketing content')
    optimize_parser.add_argument('strategy_file', help='Strategy JSON file')
    optimize_parser.add_argument('content_file', help='Text file with original content')
    
    # Ethics check command
    ethics_parser = subparsers.add_parser('check-ethics', help='Check ethical compliance')
    ethics_parser.add_argument('content_file', help='Text file to analyze')
    ethics_parser.add_argument('--strategy', help='Optional strategy file for context')
    
    # Create samples command
    subparsers.add_parser('create-samples', help='Create sample files for testing')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    cli = PreSuaderCLI()
    
    # Route commands
    if args.command == 'analyze':
        cli.analyze_audience(args.input_file)
    elif args.command == 'strategy':
        cli.create_strategy(args.profile_file, args.objective)
    elif args.command == 'optimize-content':
        cli.optimize_content(args.strategy_file, args.content_file)
    elif args.command == 'check-ethics':
        cli.check_ethics(args.content_file, args.strategy)
    elif args.command == 'create-samples':
        cli.create_sample_files()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
