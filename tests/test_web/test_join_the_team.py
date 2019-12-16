import pytest

from hamcrest import all_of, assert_that, contains_string, equal_to
from libs.web.pages.join_the_team import JoinTheTeam
from tests.test_web.input_data import JOB_DATA

page = JoinTheTeam()


@pytest.mark.parametrize('keyword', ['qa', 'QA', 'QA Automation', 'Automation'])
def test_search_by_keyword_positive(keyword):
    """Tests search by keyword: job's title should match keyword"""
    page.input_keywords.send_keys(keyword)
    page.button_search.click()
    for job_listing in page.jobs_listings:
        assert_that(job_listing.title.lower(), contains_string(keyword.lower()),
                    'Job title "{0}" doesn\'t match search keyword "{1}"'.format(job_listing.title, keyword))


@pytest.mark.parametrize('keyword', ['qqq', '<h2>', '<script>alert(1)</script>', '\'WHERE 1=\'1'])
def test_search_by_keyword_negative(keyword):
    """Tests search by keyword: 'No jobs found.' message should be displayed if no job matches keyword"""
    message = 'No jobs found.'
    page.input_keywords.send_keys(keyword)
    page.button_search.click()
    assert_that(page.jobs_list.text, contains_string(message))


def test_check_job_container_data():
    """Tests that correct job's data is displayed."""
    page.input_keywords.send_keys(JOB_DATA['title'])
    page.button_search.click()
    # check that job listing is displayed
    assert_that(len(page.jobs_listings), equal_to(1))
    actual_job = page.jobs_listings[0]
    assert_that(all_of([actual_job.title, equal_to(JOB_DATA['title']),
                        actual_job.location, equal_to(JOB_DATA['location']),
                        actual_job.description, contains_string(JOB_DATA['description']),
                        actual_job.type, equal_to(JOB_DATA['type']),
                        actual_job.date, equal_to(JOB_DATA['date'])]))


@pytest.mark.skip
def test_check_job_container_links():
    """Tests that links in job container work properly"""
    pass
