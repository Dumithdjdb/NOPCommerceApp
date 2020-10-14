pytest -s -v -m "sanity" --html=./reports/report_Chrome.html testCases/ --browser chrome
pytest -s -v -m "sanity" --html=./reports/report_Firefox.html testCases/ --browser firefox

rem pytest -s -v -m "sanity or regression" --html=./reports/report_Chrome.html testCases/ --browser chrome