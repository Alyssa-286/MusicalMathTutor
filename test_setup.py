# File: test_setup.py

import os
import subprocess
import sys
from dotenv import load_dotenv

def test_python_version():
    """Test Python version"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    if version >= (3, 8):
        print("✅ Python version is compatible")
        return True
    else:
        print("❌ Python 3.8+ required")
        return False

def test_dependencies():
    """Test if all Python packages are installed"""
    required_packages = [
        'google.generativeai',
        'elevenlabs',
        'manim', 
        'dotenv'
    ]
    
    missing = []
    for package in required_packages:
        try:
            if package == 'dotenv':
                import dotenv # The module name is 'dotenv'
            else:
                __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is missing")
            missing.append(package)
    
    return len(missing) == 0

def test_system_tools():
    """Test system tools like FFmpeg and Manim CLI"""
    tools = {
        'ffmpeg': ['ffmpeg', '-version'],
        'manim': ['manim', '--version']
    }
    
    all_good = True
    for tool, command in tools.items():
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ {tool} is installed")
            else:
                print(f"❌ {tool} error: {result.stderr}")
                all_good = False
        except subprocess.TimeoutExpired:
            print(f"❌ {tool} timeout")
            all_good = False
        except FileNotFoundError:
            print(f"❌ {tool} not found in PATH")
            all_good = False
    
    return all_good

def test_api_keys():
    """Test if API keys are set"""
    load_dotenv()
    
    required_keys = ['GEMINI_API_KEY', 'ELEVENLABS_API_KEY']
    all_good = True
    
    for key in required_keys:
        value = os.getenv(key)
        if value and len(value) > 10:  # Basic validation
            print(f"✅ {key} is set")
        else:
            print(f"❌ {key} is missing or invalid")
            all_good = False
    
    return all_good

def test_file_structure():
    """Test if all required files exist"""
    required_files = [
        'main.py',
        'generate_content.py', 
        'music.py',
        'combiner.py',
        'musical_math_lesson.py',
        'requirements.txt'
    ]
    
    all_good = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} is missing")
            all_good = False
    
    return all_good

def test_write_permissions():
    """Test write permissions in current directory"""
    try:
        test_file = 'test_write_permissions.tmp'
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        print("✅ Write permissions OK")
        return True
    except Exception as e:
        print(f"❌ Write permission error: {e}")
        return False

def quick_api_test():
    """Quick test of API connections"""
    load_dotenv()
    
    # Test Gemini
    try:
        import google.generativeai as genai
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content("Say 'Hello, test successful!'")
            if response.text:
                print("✅ Gemini API connection successful")
            else:
                print("❌ Gemini API returned empty response")
        else:
            print("⚠️ Skipping Gemini API test (no key)")
    except Exception as e:
        print(f"❌ Gemini API test failed: {e}")
    
    # Test ElevenLabs
    try:
        from elevenlabs.client import ElevenLabs
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if api_key:
            client = ElevenLabs(api_key=api_key)
            voices = client.voices.get_all()
            if voices:
                print("✅ ElevenLabs API connection successful")
            else:
                print("❌ ElevenLabs API returned no voices")
        else:
            print("⚠️ Skipping ElevenLabs API test (no key)")
    except Exception as e:
        print(f"❌ ElevenLabs API test failed: {e}")

def main():
    """Run all tests"""
    print("🧪 Musical Math Teacher - Setup Test")
    print("=" * 50)
    
    tests = [
        ("Python Version", test_python_version),
        ("Python Dependencies", test_dependencies),
        ("System Tools", test_system_tools),
        ("File Structure", test_file_structure),
        ("Write Permissions", test_write_permissions),
        ("API Keys", test_api_keys),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            results.append(False)
    
    # API tests (separate since they can be slow)
    print(f"\n🔍 Testing API Connections...")
    try:
        quick_api_test()
    except Exception as e:
        print(f"❌ API tests failed: {e}")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! You're ready to use Musical Math Teacher.")
        print("\nNext steps:")
        print("1. Make sure your .env file has valid API keys")
        print("2. Run: python main.py")
        print("3. Choose a math concept and create your first lesson!")
    else:
        print(f"⚠️ {total - passed} out of {total} tests failed.")
        print("\nPlease fix the issues above before proceeding.")
        print("Refer to the README.md for detailed setup instructions.")
    
    print(f"\nTest Results: {passed}/{total} passed")

if __name__ == "__main__":
    main()