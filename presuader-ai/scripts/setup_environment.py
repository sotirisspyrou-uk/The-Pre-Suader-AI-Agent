#!/usr/bin/env python3
# /scripts/setup_environment.py
# Version: 08-09-2025 17:40:00
# Pre-Suader AI Agent - Environment Setup
# Author: Sotiris Spyrou, CEO, VerityAI

import subprocess
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        print(f"   Current version: {sys.version}")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def run_tests():
    """Run basic tests"""
    print("🧪 Running tests...")
    try:
        result = subprocess.run([sys.executable, "tests/test_basic.py"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Tests passed")
            return True
        else:
            print(f"⚠️  Some tests failed:\n{result.stdout}")
            return False
    except Exception as e:
        print(f"❌ Test execution failed: {e}")
        return False

def create_sample_files():
    """Create sample files for testing"""
    print("📁 Creating sample files...")
    try:
        subprocess.run([sys.executable, "src/presuader_cli.py", "create-samples"], 
                      check=True, capture_output=True)
        print("✅ Sample files created")
        return True
    except subprocess.CalledProcessError:
        print("⚠️  Could not create sample files automatically")
        return False

def main():
    """Main setup routine"""
    print("🚀 Pre-Suader AI Agent - Environment Setup")
    print("=" * 50)
    
    steps = [
        ("Python Version Check", check_python_version),
        ("Install Dependencies", install_dependencies),
        ("Create Sample Files", create_sample_files),
        ("Run Basic Tests", run_tests)
    ]
    
    for step_name, step_func in steps:
        print(f"\n⏳ {step_name}...")
        if not step_func():
            print(f"❌ Setup failed at: {step_name}")
            return False
    
    print("\n" + "=" * 50)
    print("🎉 Environment setup complete!")
    print("\n📚 Quick start commands:")
    print("   python src/presuader_cli.py demo")
    print("   python src/presuader_cli.py analyze sample_audience.json")
    print("\n📖 See README.md for complete documentation")
    print("📦 See CORE_FILES_NOTE.md for full implementation details")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
