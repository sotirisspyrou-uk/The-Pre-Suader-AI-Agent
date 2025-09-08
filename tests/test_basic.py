# /tests/test_basic.py
# Version: 08-09-2025 17:40:00
# Pre-Suader AI Agent - Basic Tests
# Author: Sotiris Spyrou, CEO, VerityAI

import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def test_imports():
    """Test that core modules can be imported"""
    try:
        from presuader_core_functions import PreSuaderCore, AudienceProfile
        from metrics_tracker import MetricsTracker
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality works"""
    try:
        from presuader_core_functions import PreSuaderCore
        
        presuader = PreSuaderCore()
        
        # Test audience analysis
        test_data = {
            "segment_name": "Test Segment",
            "demographics": {"industry": "tech"},
            "tech_savvy": True,
            "values": ["innovation"]
        }
        
        profile = presuader.analyze_audience_psychology(test_data)
        assert profile.segment_name == "Test Segment"
        
        print("✅ Basic functionality test passed")
        return True
        
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        return False

def test_cli_interface():
    """Test CLI interface works"""
    try:
        import subprocess
        result = subprocess.run([
            sys.executable, "src/presuader_cli.py", "--help"
        ], capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print("✅ CLI interface test passed")
            return True
        else:
            print(f"❌ CLI test failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ CLI test error: {e}")
        return False

def run_all_tests():
    """Run all basic tests"""
    print("🧪 Running Pre-Suader basic tests...")
    
    tests = [
        ("Import Test", test_imports),
        ("Functionality Test", test_basic_functionality),
        ("CLI Interface Test", test_cli_interface)
    ]
    
    passed = 0
    for name, test_func in tests:
        print(f"\n🔍 {name}:")
        if test_func():
            passed += 1
    
    print(f"\n📊 Test Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed!")
        return True
    else:
        print("⚠️  Some tests failed - check implementations")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
