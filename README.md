![Scrapinghub logo](scrapinghub.png)

# Trial Project: Product spider #

### Goal ###

The goal of this trial project is to create a spider with Scrapy to scrape artistic work information from a museum (pstrial-2017-12-18.toscrape.com). The specs are detailed below.

**Note:** This spider and the website it scrapes are only for the test and have no commercial value.

### Product spider ###

Create a Python 3.5+ spider to scrape all works in the In Sunsh and Summertime categories on http://pstrial-2018-05-21.toscrape.com/ .
It should navigate down the work browse tree (e.g.: Summertime / Wrapper From / Barn Owl) to the lowest level and parse on a per-work basis.

If a work does not have information for a specific field, please omit the field.

Fields:

* url: (string) Url of the work being scraped
* artist: (list of strings) List of artists for the work
* title: (string) Title of the work
* image: (string) URL of the image
* height: (float) Physical height in cm, only if available in cm
* width: (float) Physical width in cm, only if available in cm
* description: (string) Description of the work
* path: (string list) The names of categories visited to reach the item via the browse tree. Ex: ["Summertime", "Wrapper From", "Ao Shu"]

### Deliverable ###

You have been given access to this private repository on bitbucket to deliver the code of this trial.

The spider should be written in Python 3.5+ and follow the PEP8 style guidelines.  Please commit shub's scrapinghub.yml file (with any sensitive information removed).  You should also run your completed spider in the cloud - you will receive an email with an invitation to a Scrapy Cloud project for this purpose (if you don't, please let us know).  Instructions for deploying with Python 3 can be found here: https://helpdesk.scrapinghub.com/support/solutions/articles/22000200387-deploying-python-3-spiders-to-scrapy-cloud


Please keep the followings points in mind when delivering your code:

1. Commit History. Don’t worry about delivering a clean commit history, do as many commits as you would do while working normally. Please do not squash everything into a single commit, we use the commit history to review the evolution of your work.
2. Code quality. The final version of your code will be considered finished and production-ready - please make sure the spider results are complete and look correct upon inspection. You can check the [online documentation](https://doc.scrapy.org) to learn about Scrapy's features and best practices.
3. Spent time report. Please use the file `tasklog.yml` to list the tasks you worked on and the time you worked on them. The format for the entries (YAML) is described in the comments on the file. You can be as detailed as you want, but a summary of high-level points is often enough (learning scrapy, spider design, implementation, testing, etc). Keep in mind that this is not a time competition, a clean implementation is preferable over a quick one. The
4. Assumptions and decisions report.  Please document assumptions you made and reasons for decisions you made in a file called `assumptions.txt` in your repository (you may also use the `.md` or `.rst` formats if you like).  We will refer to this file if your code contains things we did not expect.

### Time limit ###

We expect this project to take around 8-10 hours depending on your level of experience.  We don't want you to over-invest yourself in this project, so if you're still working after spending 16 hours please stop and submit what you've completed.

### Deadlines ###

This project doesn’t have a deadline. Just submit the results as soon as you have them ready (but no sooner) including the spent time report. The sooner you submit, the sooner we will move to the next step.

### Confidentiality ###

Please don’t share code or specifications about this project with anyone outside Scrapinghub.
