from pathlib import Path

def save_screenshot(driver, test_name):

    screenshot_dir = Path("screenshots")
    screenshot_dir.mkdir(exist_ok=True)

    file_path = screenshot_dir / f"{test_name}.png"

    driver.save_screenshot(str(file_path))

    return file_path