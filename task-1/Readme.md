# TASK

Your goal is to parse the Date from a remark string. The string contains year, month and day somewhere. Write a function parseDate() that is supposed to take a remark string as input and return a formatted Date (YYYY-MM-DD). The function contains a regex (var regex) to
parse the pattern. It is your task to correct the code.


The regex is case insensitive and searches for a pattern to parse the year, month and day.
- year: any four digit number after the word 'year'
- month: any two or one digit number after the word 'month'
- day: any two or one digit number after the word 'day'


For example:
Input string:
HGI_YEAR2019testmonth12DATE12ABU1234DAY23
Output: 2019-12-23