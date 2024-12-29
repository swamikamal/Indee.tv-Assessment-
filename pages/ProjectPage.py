#ProjectPage.py
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.utils.selenium_utils import (
    wait_for_element_to_be_clickable,
    wait_for_element_to_be_present,
    wait_for_element_to_be_visible
)

class ProjectPage:
    def __init__(self, driver, project_name='Test automation project'):
        self.driver = driver
        self.validate_project_name = project_name

        # Locators
        self.current_page_title_text = (By.XPATH, '//*[@id="genre-sorter"]/div/div[1]/p')
        self.test_automation_project_text = (By.XPATH, '//*[@id="indee-title-card-prj-01j912ej0rs3wwadvadhavpasx"]/div[2]/h5')
        self.current_project_name_text = (By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/div[2]/div/div[1]/div/div/div/p')
        self.details_tab = (By.XPATH, '//*[@id="detailsSection"]')
        self.videos_tab = (By.XPATH, '//*[@id="videosSection"]')
        self.play_button = (By.XPATH, '//*[@id="vid-01j912gbvdnr5er79gqeb8k30w"]/div/div[1]/button[1]')

        self.video_frame = (By.XPATH, "//*[@id='video_player']")
        self.pause_button = (By.XPATH,'//*[@id="media-player"]/div[2]/div[12]/div[1]/div/div/div[2]/div')
        self.continue_watching_button = (By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/dialog/div[2]/div[1]/div/div[1]/button')
        self.video_player = (By.XPATH,'//*[@id="media-player"]/div[2]/div[4]/video')
        self.continue_button = (By.CSS_SELECTOR, "button.continue-watching")
        self.continue_watching_text = (By.XPATH, '//*[@id="__nuxt"]/div/div/div[2]/dialog/div[2]/div[1]/div/div[1]/p')
        self.video_player_playback_button = (By.XPATH, '//*[@id="media-player"]/div[2]/div[13]/div[4]/div[2]/div[1]')
        self.video_elapsed =(By.XPATH,'//*[@id="media-player"]/div[2]/div[13]/div[4]/div[2]/div[8]')

        self.video_mute_volume_button = (By.XPATH,'//*[@id="media-player"]/div[2]/div[13]/div[4]/div[2]/div[4]')
        self.video_volume_slider = (By.XPATH, '//*[@id="media-player"]/div[2]/div[13]/div[4]/div[2]/div[4]/div/div/div')
        self.video_volume_knob = (By.XPATH, '//*[@id="media-player"]/div[2]/div[13]/div[4]/div[2]/div[4]/div/div/div/div[4]')
        self.video_volume_slider_progress = (By.XPATH,'//*[@id="media-player"]/div[2]/div[13]/div[4]/div[2]/div[4]/div')

        self.settings_button = (By.XPATH, '//*[@id="media-player"]/div[2]/div[13]/div[4]/div[2]/div[14]')
        self.resolution_option_480p_button = (By.XPATH, '//*[@id="jw-settings-submenu-quality"]/div/button[3]')
        self.resolution_option_720p_button = (By.XPATH, '//*[@id="jw-settings-submenu-quality"]/div/button[2]')

        self.back_button = (By.XPATH,'//*[@id="__nuxt"]/div/div/div[2]/dialog/div[1]/button')
        self.video_frame = (By.XPATH, "//*[@id='video_player']")

        self.side_bar_button = (By.XPATH,'//*[@id="signOutSideBar"]')
        self.sign_in_button = (By.XPATH,'//*[@id="sign-in-button"]')

    def open_project(self):
        """Open the test automation project."""
        wait_for_element_to_be_clickable(self.driver, self.test_automation_project_text).click()

    def switch_to_details_tab(self):
        """Switch to the details tab."""
        wait_for_element_to_be_clickable(self.driver, self.details_tab).click()

    def switch_to_videos_tab(self):
        """Switch to the videos tab."""
        wait_for_element_to_be_clickable(self.driver, self.videos_tab).click()

    def play_video(self):
        """Play the video."""
        wait_for_element_to_be_clickable(self.driver, self.play_button).click()

    def pause_video(self):
        video_frame = wait_for_element_to_be_present(self.driver, self.video_frame)
        self.driver.switch_to.frame(video_frame)

        # Move to playback
        video_player_playback_button = wait_for_element_to_be_present(self.driver, self.video_player_playback_button,delay=0)
        actions = ActionChains(self.driver)
        actions.move_to_element(video_player_playback_button).click().perform()

        self.driver.switch_to.default_content()

    def pause_video_in(self, delay):
        try:
            # Wait for the frame containing the video and switch to it
            video_frame = wait_for_element_to_be_present(self.driver, self.video_frame)
            self.driver.switch_to.frame(video_frame)

            # Locate the video elapsed time element once
            video_elapsed_element = wait_for_element_to_be_present(self.driver, self.video_elapsed)

            # Track start time to implement a timeout
            start_time = time.time()
            timeout = 12  # 12 seconds timeout

            # Loop until the video elapsed time matches the delay
            while True:
                current_time = video_elapsed_element.get_attribute("textContent").strip()

                # Check if the current time matches the delay
                if current_time == delay:
                    # Click to pause the video and print confirmation
                    video_player_playback_button = wait_for_element_to_be_present(self.driver, self.video_player_playback_button,delay=0)
                    actions = ActionChains(self.driver)
                    actions.move_to_element(video_player_playback_button).click().perform()
                    print("Video paused at specified delay.")
                    break

                # Break if timeout is reached
                if time.time() - start_time > timeout:
                    print("Timeout reached without matching the delay.")
                    break

        except Exception as e:
            print(f"Error pausing video: {e}")
            # Handle the error, e.g., log the error, take a screenshot, or retry the action

        finally:
            self.driver.switch_to.default_content()


    def continue_watching(self):
        """Continue watching the video."""
        wait_for_element_to_be_clickable(self.driver, self.continue_watching_button).click()


    def adjust_volume(self):
        """Adjust the volume of the video to 50%."""
        # Somehow, i was unable to get to the exact 50%. so created this :-)
        # Switch to the iframe containing the video player
        video_frame = wait_for_element_to_be_present(self.driver, self.video_frame)
        self.driver.switch_to.frame(video_frame)

        # Move to Volume
        actions = ActionChains(self.driver)
        volume_button = wait_for_element_to_be_present(self.driver, self.video_mute_volume_button, delay=0)
        actions.move_to_element(volume_button).perform()

        # Locate the volume slider container and knob elements
        volume_slider_container = wait_for_element_to_be_visible(self.driver, self.video_volume_slider,delay=0.2)
        volume_slider_knob = wait_for_element_to_be_visible(self.driver, self.video_volume_knob,delay=0.2)

        volume_overlay = wait_for_element_to_be_present(self.driver,self.video_volume_slider_progress,delay=0.3)

        # Loop to adjust volume in small increments until it reaches approximately 50%
        target_volume = 50.0  # Target volume percentage
        current_volume = float(volume_overlay.get_attribute('aria-valuenow'))

        while abs(current_volume - target_volume) > 0.0000000000001:
            # Determine the direction to move the knob
            step = 1 if abs(current_volume - target_volume) < 2 else 4
            if current_volume < target_volume:
                # Move up
                actions.click_and_hold(volume_slider_knob).move_by_offset(0, -step).release().perform()
            else:
                # Move down
                actions.click_and_hold(volume_slider_knob).move_by_offset(0, step).release().perform()

            # Re-check the current volume after adjustment
            current_volume = float(volume_overlay.get_attribute('aria-valuenow'))

        # Switch back to the main content
        self.driver.switch_to.default_content()



    def change_resolution(self, resolution):
        """Change the video resolution."""
        video_frame = wait_for_element_to_be_present(self.driver, self.video_frame)
        self.driver.switch_to.frame(video_frame)

        # Open setting
        actions = ActionChains(self.driver)
        goto_settings = wait_for_element_to_be_present(self.driver, self.settings_button,delay=0)
        actions.move_to_element(goto_settings).click().perform()

        # Changing resolution
        resolution_option = self.resolution_option_720p_button if resolution == '720' else self.resolution_option_480p_button
        wait_for_element_to_be_clickable(self.driver, resolution_option,delay=0.2).click()

        # Close setting
        actions.move_to_element(goto_settings).click().perform()

        # Back to default structure
        self.driver.switch_to.default_content()


    def navigate_back(self):
        """Navigate back to the previous page."""
        wait_for_element_to_be_clickable(self.driver, self.back_button).click()

    def sign_out(self):
        """Navigate and sign_out"""
        wait_for_element_to_be_clickable(self.driver,self.side_bar_button).click()



    def is_current_page_loaded(self):
        """Check if the current page is loaded."""
        return wait_for_element_to_be_visible(self.driver, self.current_page_title_text) is not None

    def is_project_name_correct_before_opening(self):
        """Check if the project name is correct before opening."""
        current_project_name = wait_for_element_to_be_visible(self.driver, self.test_automation_project_text).text
        return current_project_name == self.validate_project_name

    def is_project_loaded(self):
        """Check if the project page is loaded."""
        return wait_for_element_to_be_visible(self.driver, self.current_project_name_text) is not None

    def is_project_name_correct_after_loading(self):
        """Check if the project name is correct after loading."""
        current_project_name = wait_for_element_to_be_visible(self.driver, self.current_project_name_text).text
        return current_project_name == self.validate_project_name

    def is_tab_active(self, tab_name):
        """Check if the specified tab is active."""
        active_tabs = {
            "Details": self.details_tab,
            "Videos": self.videos_tab
        }
        return tab_name in active_tabs and wait_for_element_to_be_visible(self.driver, active_tabs[tab_name]) is not None

    def is_video_playing(self):
        """Check if the video is currently playing."""
        video_frame = wait_for_element_to_be_present(self.driver, self.video_frame,delay=2)
        self.driver.switch_to.frame(video_frame)

        video_elapsed_element = wait_for_element_to_be_present(self.driver, self.video_elapsed,delay=2)
        current_time = video_elapsed_element.get_attribute("textContent").strip()
        self.driver.switch_to.default_content()
        return str(current_time) == '00:14'

    def is_video_paused(self):
        """Check if the video is currently paused."""
        check_video_status = wait_for_element_to_be_visible(self.driver, self.continue_watching_text,timeout=20).text
        return check_video_status == 'Continue Watching'

    def is_volume_changed(self):
        video_frame = wait_for_element_to_be_present(self.driver, self.video_frame,delay=0)
        self.driver.switch_to.frame(video_frame)
        volume_overlay = wait_for_element_to_be_present(self.driver,self.video_volume_slider_progress,delay=0.2)
        volume_value = volume_overlay.get_attribute('aria-valuenow')
        self.driver.switch_to.default_content()
        return volume_value == '50'

    def is_resolution_set(self, expected_resolution):
        """Check if the video resolution is set to the expected resolution."""
        video_frame = wait_for_element_to_be_present(self.driver, self.video_frame)
        self.driver.switch_to.frame(video_frame)

        actions = ActionChains(self.driver)
        goto_settings = wait_for_element_to_be_present(self.driver, self.settings_button,delay=0)
        actions.move_to_element(goto_settings).click().perform()

        button_element = (
            wait_for_element_to_be_present(self.driver, self.resolution_option_720p_button)
            if expected_resolution == '720' else
            wait_for_element_to_be_present(self.driver, self.resolution_option_480p_button)
            if expected_resolution == '480' else None
        )
        current_resolution = button_element.get_attribute("aria-checked")
        self.driver.switch_to.default_content()
        return current_resolution == 'true'

    def is_logged_out(self):
        """Check if on the all titles page."""
        return wait_for_element_to_be_clickable(self.driver,self.sign_in_button) is not None
