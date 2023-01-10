from bs4 import BeautifulSoup


def parse(markup):
    soup = BeautifulSoup(markup, "html.parser")

    courses = soup.select(".calendar-event")

    course_info = "Course Info\n\n"

    # Note: with requests need to check if "Python" in course.h1.text:
    # this is needed at because of the "invisible" text coming through
    # with Playwright this isn't an issue

    for course in courses:
        course_info += course.h1.text + "\n"
        course_info += course.h2.text + "\n"
        course_info += "\n"

    return course_info
