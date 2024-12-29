# test_video_playback_and_control.py
import logging
PIN = "WVMVHWBS"
logging.basicConfig(level=logging.INFO)

def test_current_page_loaded(project_page):
    assert project_page.is_current_page_loaded(), "Failed to load the current page."

def test_check_project_name_cart(project_page):
    assert project_page.is_project_name_correct_before_opening(), "Failed to locate the Test Automation Project."

def test_navigate_to_project(project_page):
    project_page.open_project()  # Ensure you open the project before checking
    assert project_page.is_project_loaded(), "Failed to locate the Test Automation Project."

def test_check_correct_project_name(project_page):
    assert project_page.is_project_name_correct_after_loading(), "Failed to locate the Test Automation Project."

def test_switch_to_details_tab(project_page):
    project_page.switch_to_details_tab()
    assert project_page.is_tab_active("Details"), "Details tab did not open properly."

def test_switch_back_to_videos_tab(project_page):
    project_page.switch_to_videos_tab()
    assert project_page.is_tab_active("Videos"), "Failed to switch back to Videos tab."

def test_play_and_pause_video(project_page):
    project_page.play_video()
    project_page.pause_video_in('00:10')
    assert project_page.is_video_paused(), "Failed to play and pause video just after 00:10."

def test_continue_watching(project_page):
    project_page.continue_watching()
    assert project_page.is_video_playing(), "Continue Watching failed to resume playback."

def test_adjust_volume(project_page):
    project_page.adjust_volume()  # Set volume to 50%
    assert project_page.is_volume_changed(), "Volume not set to 50%."

def test_change_resolution(project_page):
    project_page.change_resolution('480')
    assert project_page.is_resolution_set('480'), "Resolution change to 480p failed."
    project_page.change_resolution('720')
    assert project_page.is_resolution_set('720'), "Resolution change to 720p failed."

def test_pause_and_exit(project_page):
    project_page.pause_video()
    project_page.navigate_back()
    assert project_page.is_project_loaded(), "Failed to exit the project."

def test_logout(project_page):
    project_page.sign_out()
    assert project_page.is_logged_out(), "Logout failed or Sign In page not visible."
