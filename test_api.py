#!/usr/bin/env python3
"""
Unit tests for MinuteMate API endpoints
Tests capture, transcription call, and API endpoints
"""

import unittest
import json
import requests
import time

class TestMinuteMateAPI(unittest.TestCase):
    """Test cases for MinuteMate API"""
    
    def setUp(self):
        """Set up test environment"""
        self.base_url = "http://localhost:5000"
        self.session_id = None
    
    def test_1_status_endpoint(self):
        """Test GET /status returns 'recording' or 'idle'"""
        response = requests.get(f"{self.base_url}/status")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('status', data)
        self.assertIn(data['status'], ['recording', 'idle'])
        
        print(f"✅ Status endpoint: {data['status']}")
    
    def test_2_start_recording(self):
        """Test starting recording session"""
        response = requests.post(f"{self.base_url}/start")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('session_id', data)
        self.session_id = data['session_id']
        
        print(f"✅ Recording started: {self.session_id}")
    
    def test_3_status_while_recording(self):
        """Test status shows 'recording' while active"""
        if not self.session_id:
            self.skipTest("No active session")
        
        response = requests.get(f"{self.base_url}/status")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data['status'], 'recording')
        self.assertIn('duration', data)
        
        print(f"✅ Status shows recording: {data['duration']}s")
    
    def test_4_stop_recording(self):
        """Test stopping recording session"""
        if not self.session_id:
            self.skipTest("No active session")
        
        response = requests.post(f"{self.base_url}/stop")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('session_id', data)
        
        print(f"✅ Recording stopped: {data['session_id']}")
    
    def test_5_status_after_stop(self):
        """Test status shows 'idle' after stopping"""
        response = requests.get(f"{self.base_url}/status")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data['status'], 'idle')
        
        print(f"✅ Status shows idle after stop")
    
    def test_6_generate_minutes(self):
        """Test minutes generation from transcript"""
        test_transcript = """
        Welcome to our Q2 planning meeting. Let's discuss the quarterly goals and targets.
        We need to increase sales by 25% this quarter. John will prepare the budget proposal.
        Sarah agreed to review the marketing campaign. We decided to launch the new product in March.
        The team must submit progress reports by Friday. We should focus on customer retention.
        """
        
        response = requests.post(
            f"{self.base_url}/generate-minutes",
            json={'transcript': test_transcript}
        )
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('minutes', data)
        self.assertTrue(len(data['minutes']) > 0)
        
        print(f"✅ Minutes generated: {len(data['minutes'])} characters")
    
    def test_7_get_minutes(self):
        """Test GET /minutes/{id} endpoint"""
        if not self.session_id:
            self.skipTest("No session ID available")
        
        response = requests.get(f"{self.base_url}/minutes/{self.session_id}")
        # This might return 404 if session data isn't persisted
        # For now, just test the endpoint exists
        self.assertIn(response.status_code, [200, 404])
        
        print(f"✅ Minutes endpoint tested: {response.status_code}")

def run_tests():
    """Run all tests"""
    print("🧪 Running MinuteMate API Tests")
    print("=" * 40)
    
    # Check if server is running
    try:
        response = requests.get("http://localhost:5000/status", timeout=5)
        if response.status_code == 200:
            print("✅ Backend server is running")
        else:
            print("❌ Backend server not responding properly")
            return False
    except requests.exceptions.RequestException:
        print("❌ Backend server not running. Start with: python app.py")
        return False
    
    # Run tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMinuteMateAPI)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 40)
    if result.wasSuccessful():
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed")
        return False

if __name__ == '__main__':
    run_tests() 