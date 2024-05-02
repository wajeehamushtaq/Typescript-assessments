function parseDate(remark: string): string{
    const  regex = /year(\d{4}).*?month(\d{1,2}).*?day(\d{1,2})/i

    const  match = regex.exec(remark) // searches a string for a specified pattern, and returns the found text as an object.
    console.log(match)

    if(match !== null){
        const year = match[1]
        const month = match[2]
        const day = match[3]

        return `${year}-${month}-${day}`
    }
    else{
        return 'Date cannot be found'
    }

}


const remark = "HGI_YEAR2019testmonth12DATE12ABU1234DAY23"
const date = parseDate(remark)
console.log(date)


// This regular expression /year(\d{4}).*?month(\d{1,2}).*?day(\d{1,2})/i is designed to match patterns in a string that represent a date in the format "year-month-day", where:
// year(\d{4}): Matches the word "year" followed by exactly four digits (\d{4}), capturing the four digits as a group.
// .*?: Matches any character (.) zero or more times (*), non-greedily (?), meaning it will match as few characters as possible before the next part of the pattern.
// month(\d{1,2}): Matches the word "month" followed by one or two digits (\d{1,2}), capturing the digits as a group.
// .*?: Matches any character (.) zero or more times (*), non-greedily (?).
// day(\d{1,2}): Matches the word "day" followed by one or two digits (\d{1,2}), capturing the digits as a group.
// The i flag at the end of the regular expression makes it case-insensitive, so it will match variations in capitalization (e.g., "Year", "Month", "Day").