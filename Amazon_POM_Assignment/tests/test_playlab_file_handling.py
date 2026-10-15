from pathlib import Path

from playwright.sync_api import Page, expect


class TestPlayLabFileHandling:

    URL = "https://playwrightlab.github.io/"

    CSV_FILE = (
        Path.home()
        / "Downloads"
        / "Inventory Management (1).csv"
    )

    def test_single_file_upload(self, page: Page):
        assert self.CSV_FILE.is_file(), (
            f"CSV file not found: {self.CSV_FILE}"
        )

        page.goto(self.URL)

        # Select the single-file upload input
        file_input = page.locator('input[type="file"]').nth(0)
        file_input.set_input_files(str(self.CSV_FILE))

        # Click the first Upload button
        page.get_by_role("button", name="Upload").nth(0).click()

        # Verify upload success and filename
        expect(
            page.get_by_text("Uploaded successfully!", exact=True)
        ).to_be_visible()

        expect(
            page.get_by_text(
                "Inventory Management (1).csv", exact=True
            )
        ).to_be_visible()

    def test_multiple_file_upload(
        self, page: Page, tmp_path: Path
    ):
        assert self.CSV_FILE.is_file(), (
            f"CSV file not found: {self.CSV_FILE}"
        )

        # Create a second file for multiple-file upload
        second_file = tmp_path / "second_test_file.txt"
        second_file.write_text("Second file for upload testing")

        page.goto(self.URL)

        # Select the multiple-file upload input
        file_input = page.locator('input[type="file"]').nth(1)

        file_input.set_input_files(
            [str(self.CSV_FILE), str(second_file)]
        )

        # Click the second Upload button
        page.get_by_role("button", name="Upload").nth(1).click()

        # Verify upload success and both filenames
        expect(
            page.get_by_text("Uploaded successfully!", exact=True)
        ).to_be_visible()

        expect(
            page.get_by_text(
                "Inventory Management (1).csv", exact=True
            )
        ).to_be_visible()

        expect(
            page.get_by_text("second_test_file.txt", exact=True)
        ).to_be_visible()

    def test_download_pdf(self, page: Page, tmp_path: Path):
        page.goto(self.URL)

        # Wait for the download before clicking
        with page.expect_download() as download_info:
            page.get_by_role("button", name="Download PDF").click()

        download = download_info.value

        # Save the downloaded PDF
        pdf_path = tmp_path / download.suggested_filename
        download.save_as(str(pdf_path))

        # Verify the downloaded file
        assert pdf_path.is_file()
        assert pdf_path.stat().st_size > 0
        assert pdf_path.suffix.lower() == ".pdf"

    def test_open_pdf(self, page: Page):
        page.goto(self.URL)

        # Wait for the PDF to open in a new tab
        with page.expect_popup() as popup_info:
            page.get_by_role("button", name="Open PDF").click()

        pdf_page = popup_info.value

        # Verify the new tab opened
        expect(pdf_page).to_have_url(
            lambda url: ".pdf" in url.lower()
        )

        assert pdf_page.url != page.url
