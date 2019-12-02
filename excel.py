--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 166 - Convert a Number to Weekday Name
By eforexcel|Saturday, November 18th, 2017|Categories: Tips and Tricks|Tags: Calendar, Day, month, WEEKDAY, WeekNum, year|0 Comments

Suppose you want to return 1 = Sunday, 2 = Monday…..7 = Saturday

=TEXT(A1&"Jan2017","dddd")

To show only 3 characters of the Weekday Name

=TEXT(A1&"Jan2017","ddd")

You can add a number to A1 if you want to show some other Weekday Name

Say, if you want to show 1 = Monday, 2 = Tuesday…….7 = Sunday, just add 1 to A1

=TEXT(A1+1&"Jan2017","dddd")

Say, if you want to show 1 = Friday, 2 = Saturday…….7 = Thursday, just add 5 to A1

=TEXT(A1+5&"Jan2017","dddd")

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 165 - Convert Weekday Names to Numbers
By eforexcel|Saturday, November 04th, 2017|Categories: Tips and Tricks|Tags: Calendar, Friday, Monday, Saturday, Sunday, Thursday, Tuesday, Wednesday, Week, WEEKDAY|0 Comments

Suppose Cell A2 contains weekday names like Sunday, Monday.....(or Sun, Mon...), then following formula can be used to return the numbers. Sunday will be 1 and Saturday will be 7.

=ROUND(SEARCH(LEFT(A2,2),"SuMoTuWeThFrSa")/2,0)

=MATCH(LEFT(A2,2),{"Su","Mo","Tu","We","Th","Fr","Sa"},0)

If we want to return some other number to weekdays, then formula can be tweaked accordingly. For example, to make Mon = 1 and Sun = 7

=ROUND(SEARCH(LEFT(A2,2),"MoTuWeThFrSaSu")/2,0)

=MATCH(LEFT(A2,2),{"Mo","Tu","We","Th","Fr","Sa","Su"},0)

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 162 - Convert a Month Name to Month Number
By eforexcel|Sunday, September 03rd, 2017|Categories: Tips and Tricks|Tags: Apr, April, Aug, August, Day of Week, Dec, December, Feb, Feburary, Jan, January, Jul, July, Jun, June, Mar, March, May, month, Nov, November, Oct, October, Sep, September, text, year|0 Comments

Suppose, you have text denoting month in cell A1. Let's say A1 = "Sep" or A1="September", then you can use following formula to convert this to month number

=MONTH(1&A1)

=--TEXT(1&A1,"m")

In case, cell A1 contains  the partial month name say "Septe", then in place of A1 in the above formulas, you can write LEFT(A1,3).

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 156 - Get Workbook's Directory from Formula
By eforexcel|Saturday, February 18th, 2017|Categories: Tips and Tricks|Tags: Directory, Path, Workbook, Worksheet|0 Comments

If your workbook is located in say C:\Excel\MyDocs, the formula to retrieve the directory for this would be

=LEFT(CELL("filename",A1),FIND("[",CELL("filename",A1))-2)

Note - For this formula to work, you workbook must be saved at least once.


--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 145 - Determine the First Sunday or any other Day given Weeknumber
By eforexcel|Saturday, September 17th, 2016|Categories: Tips and Tricks|Tags: Day of the Week, Friday, ISO, Monday, Saturday, Sunday, Thursday, Tuesday, Wednesday, Weeknumber|0 Comments

If you have been given a week number and has been asked to find the first Sunday for that week, you can use following formula

=CEILING(("1JAN"&A1)-14,7)+8+7*(5-1)

Where A1 has the year say A1=2016

5 is the Week Number which you can replace.

For Finding Monday, add 1 in the formula, add 2 for Tuesday and so on.

The above formula assumes that WEEKNUM function has Sunday as the starting day for the week. If you have any other day for the week as the starting day of the week, you will have to customize the above formula as per the need.

Tips and Tricks 142 - Determine Number of Working Days in a Year
By eforexcel|Saturday, August 06th, 2016|Categories: Tips and Tricks|Tags: Calendar, Holidays, Leave, Networkdays, Networkdays.Intl, Weekends, Workdays, WORKDAYS.INTL|1 Comment

Suppose, you have been given a year in A1 (Say A1 = 2016) and you need to determine the number of working days in a Year, then your formula to determine number of working days would be -

=NETWORKDAYS("1JAN"&A1,"31DEC"&A1)

The above formula is based on the fact that Saturdays and Sundays are weekends. Starting Excel 2010, you can control the weekends in the formula and function is NETWORKDAYS.INTL

=NETWORKDAYS.INTL("1JAN"&A1,"31DEC"&A1,"0000110")

In the string "000110" - First digit is Monday and last digit is Sunday. 1 defines that particular day as weekend.

If you have got your list of holidays in a range say B1:B20 (B1:B20 should contain dates in date format), you can have following formulas

=NETWORKDAYS("1JAN"&A1,"31DEC"&A1,B1:B20)

=NETWORKDAYS.INTL("1JAN"&A1,"31DEC"&A1,"0000110",B1:B20)

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 140 - Multiple Hyperlinks within Excel Text Box
By eforexcel|Saturday, July 09th, 2016|Categories: Tips and Tricks|Tags: Align, Group, Hyperlinks, Links, Text Box, vba|0 Comments

You created a Text Box and you put many words inside that say Yahoo, IBM, Microsoft etc...Now, you have given respective hyperlinks to them. But if you try to click on any hyperlink inside the text box, it will always open only one hyperlink.

It is possible to circumvent this behavior by work-around. You can execute following steps

1. Create a Text Box where you want to put all Hyperlinks.
2. Create many new Text Boxes.
3. Put the words in Text Boxes which you created in step 2 and give them Hyperlinks.
4. Drag the Text Boxes of Step 3 into Step 1 Text Box.
5. Align them properly and format them to remove borders.
6. Select all Text Boxes along with Step 1 Text Box > Page Layout > Group
7. Now, all individual Hyperlinks can be clicked separately.

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 134 - Last Working Day of the Year
By eforexcel|Saturday, April 16th, 2016|Categories: Tips and Tricks|Tags: Calendar, Day, First, Last, WORKDAY, Working|0 Comments

If a year is given in A1 say 2016, below formula can be used to know the last working day of the year (format the result as date)

=WORKDAY("1JAN"&A1+1,-1)

The above formula assumes that your weekends are Saturday and Sunday.

But, if your weekends are different (e.g. in gulf countries), you can use following formula -

=WORKDAY.INTL("1JAN"&A1+1,-1,"0000110")

Where 0000110 is a 7 character string, 1 represents a weekend and 0 is a working day. First digit is Monday and last digit is Sunday. The above example is for Gulf countries where Friday and Saturday are weekends.

You also have option to give a range which has holidays. In that case, your formula would become

=WORKDAY("1JAN"&A1+1,-1,D1:D10)

=WORKDAY.INTL("1JAN"&A1+1,-1,"0000110",D1:D10)

Where range D1:D10 contains the list of holidays.

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 133 - First Working Day of the Year
By eforexcel|Saturday, April 02nd, 2016|Categories: Tips and Tricks|Tags: Calendar, Day, EOMONTH, First, WORKDAY, Working|0 Comments

If a year is given in A1 say 2016, below formula can be used to know the first working day of the year (format the result as date)

=WORKDAY(EOMONTH("1JAN"&A1,-1),1)

The above formula assumes that your weekends are Saturday and Sunday.

But, if your weekends are different (e.g. in gulf countries), you can use following formula -

=WORKDAY.INTL(EOMONTH("1JAN"&A1,-1),1,"0000110")

Where 0000110 is a 7 character string, 1 represents a weekend and 0 is a working day. First digit is Monday and last digit is Sunday. The above example is for Gulf countries where Friday and Saturday are weekends.

You also have option to give a range which has holidays. In that case, your formula would become

=WORKDAY(EOMONTH("1JAN"&A1,-1),1,D1:D10)

=WORKDAY.INTL(EOMONTH("1JAN"&A1,-1),1,"0000110",D1:D10)

Where range D1:D10 contains the list of holidays.

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 131 - Repeat a Number and Increment and Repeat....
By eforexcel|Saturday, March 05th, 2016|Categories: Tips and Tricks|Tags: natural numbers, Repeat, sequence, series|1 Comment

Suppose, you have been given the task of repeating a number and increment that number and repeat it. For example -

1,1,1,1,2,2,2,2,3,3,3,3.....(Here, we are repeating it 4 times and incrementing and repeating 4 times again and so on)

Then you can use following formula

=ROUNDUP(ROWS($1:1)/4,0)

Suppose, you want to start the number with 5 not 1, then you can use below formula -

=ROUNDUP(ROWS($1:1)/4,0)+4

Hence, general structure of the formula is

=ROUNDUP(ROWS($1:1)/X,0)+Y-1

X - Number of times a particular number is repeated
Y - Starting Numbers

Hence, if you want to start with number 7 and you want to repeat it 5 times, then following formula should be used

=ROUNDUP(ROWS($1:1)/5,0)+6

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 128 - Used F9 to See Values in the Formula but Values Stick / Formula doesn't gets Restored
By eforexcel|Saturday, January 23rd, 2016|Categories: Tips and Tricks|Tags: Auditing, CTRL+Z, ESC, F9, Formula, Undo|0 Comments

We know that great trick that you can select part of the formula and see it values by pressing F9. See the below snip where I have selected part of the formula (see shaded area) and pressed F9 to see its values.

1

Now, if I press enter that part of the formula gets converted to values and formula doesn't get restored. (see the below snip)

1

How to Prevent this

1. If you have not pressed Enter, press ESC after using F9 to see its values and formula will get restored.

2. If you have pressed Enter, press CTRL+Z (Undo) and formula will get restored. (You need to press CTRL+Z after pressing enter. If there have been many intermediate steps, you need to press CTRL+Z repeatedly to undo this step. Of course, CTRL+Z has its own limitations in terms of retracing steps)

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 126 - Press CTRL+A Three Times to Select Entire Worksheet not Two Times
By eforexcel|Sunday, January 10th, 2016|Categories: Tips and Tricks|Tags: CTRL+A, Data, header, Range, select, shortcut, Table, Worksheet|0 Comments

The safest bet to select entire worksheet is through pressing CTRL+A three times not two times or one time, if you are using shortcut (The safest bet is to press the triangle between 1 and A as marked in Red in the given picture. The tip is for CTRL+A shortcut.)

This peculiarity of CTRL+A shortcut comes into picture when your worksheet contains tables also. Suppose, you have a worksheet like below which has at least one table.

1

1. Select a cell outside any data range, press CTRL+A and it will select entire sheet.

2. Select a cell inside A1:D2, press CTRL+A once and it will select A1:D2 range only. Pressing CTRL+A again will select entire sheet.

3. Select a cell inside header row in the table , press CTRL+A once and it will select entire table. Pressing CTRL+A again will select entire sheet.

4. Select a cell inside the table data range i.e. A6:D7, press CTRL+A once and it will select table data range i.e. A6:D7 only. Press CTRL+A again, now it will select entire table i.e. A5:D7 only not entire worksheet.. Now, press CTRL+A again i.e. 3rd time and now, it will select entire  worksheet.

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 115 - Insert Fixed Current Date and Current Time
By eforexcel|Saturday, October 31st, 2015|Categories: Tips and Tricks|Tags: Current, Date, now(), shortcut, time, today()|0 Comments

We all are aware about today() and now() formulas which insert current date and current date/timestamp. But these change with every recalculation of your worksheet.

But if you want to enter the current date and time which doesn't change with recalculation i.e. it gets fixed, then following Excel shortcuts can be used.

Current Date - CTRL+:

Current Time - CTRL+SHIFT+:

Current Date & Time - To insert the current date and time, press CTRL+; (semi-colon), then press SPACE, and then press CTRL+SHIFT+; (semi-colon).

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 114 - COUNTIF for non-contiguous range
By eforexcel|Saturday, October 17th, 2015|Categories: Tips and Tricks|Tags: COUNTIF|0 Comments

All of us love COUNTIF. And it is very easy to do - just say =COUNTIF("A1:A100",">5") and it finds all the values within the range A1 to A100 which are greater than 5. But what if I wanted the result for only A3, A8 and it should omit other cells. Try putting in following formula -

=COUNTIF((A3, A8),">5") and it will give you #VALUE error.

A possible solution is

=(A3>5)+(A8>5)

What happens if you need to do for A3, A4, A5, A8, A24, A40, A45, A89. Now, you will have to use a formula like -

=(A3>5)+(A4>5)+(A5>5)+(A8>5)+(A24>5)+(A40>5)+(A45>5)+(A89>5)

The formula becomes cumbersome as the number of cells increase. In this case, you can use below formula. This single formula can take care of contiguous (like A3:A5) and non-contiguous ranges both -

=SUM(COUNTIF(INDIRECT({"A3:A5","A8","A24","A40","A45","A89"}),">5"))

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 113 - Drag and Drop a Picture in Excel Sheet
By eforexcel|Saturday, October 17th, 2015|Categories: Tips and Tricks|Tags: Drags, Drops, insert, Object, Picture, Pictures, Sheet, Word, Worksheet|0 Comments

Try dragging and dropping a picture in a worksheet - What happens. You will notice a plug sign which means that a picture will be added. But when you release the cursor to drop the picture in Excel sheet nothing happens.

Reason - Excel doesn't support dragging and dropping the picture in a worksheet.

Now, what to do. If you are dealing with too many pictures, it is cumbersome to use Insert > Picture command.

Fortunately, there is a work around in place. Microsoft Word supports dragging and dropping of pictures. Also good thing is that, you can select all your pictures in one go and drop in Word document.

Now, you can either drag and drop the pictures from the Word document in Excel sheet or you can cut/copy and paste from Word to Excel sheet.

Side Note - OpenOffice / Libre Office supports drag and drop to their respective spreadsheet programs. (Note, but you can not drag or copy and paste pictures into Excel from Open Office / Libre Office spreadhseets like you can drag or copy / paste from Word)

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 112 - Convert a Number into Years and Months
By eforexcel|Saturday, October 03rd, 2015|Categories: Tips and Tricks|Tags: dates, INT, MOD, Months, Number, ROUND, Years|0 Comments

Suppose, you have been given a number into cell A1 say 26 and you want to display it as 2 Years and 4 Months, you can use following formula -

=INT(A1/12)&" Years and "&MOD(A1,12)&" Months"

Now, an user can become more demanding and he can say that if month is less than 12, then Years should not be displayed. For example, he might say that 8 should be converted to 8 Months and it should not be shown as 0 Years and 8 Months.

In this case, the formula would be -

=IF(INT(A1/12)>0,INT(A1/12)&" Years and ","")&MOD(A1,12)&" Months"

Now 8 will be displayed as 8 Months only not as 0 Years and 8 Months.

Now, user can ask more. He can say when I give 12, it displays as 1 Years and 0 Months and he simply wants to see 1 Years only. And for 36, he wants to see only 3 Years not 3 Years 0 Months. In this case, formula will have to be tweaked more. Now, the formula becomes -

=IF(INT(A1/12)>0,INT(A1/12)&" Years ","")&IF(MOD(A1,12)=0,"",MOD(A1,12)&" Months")

Now an user can come and can ask for one last thing. He can say that if this is 1 Year or 1 Month, it should not be displayed as Years or Months as 1 is not plural. Hence, 25 should be displayed as 2 Years and 1 Month not as 2 Years and 1 Months. Hence, 18 should not be displayed as 1 Years and 6 Months but as 1 Year and 6 Months. Similarly 13 should be displayed as 1 Year and 1 Month not as 1 Years and 1 Months.

=IF(INT(A1/12)>0,INT(A1/12)&" Year"&IF(INT(A1/12)>1,"s","")&" and ","")&MOD(A1,12)&" Month"&IF(MOD(A1,12)>1,"s","")

--------------------------------------------------------------------------------------------------------------------------------------
Tips & Tricks 107 - Autofill on a Filtered List
By eforexcel|Saturday, September 05th, 2015|Categories: Tips and Tricks|Tags: Autofill, Column, fill, natural numbers, Range, Rows, sequence, series|0 Comments

Everybody is quite aware about Autofill. There are various ways to Autofill. Refer to following article for Autofill -

Article 7 – Generate a Sequence of Numbers

Now, apply a filter on your range and all the techniques fail. If you drag, all cells are filled with 1 and no other techniques also work. The reason is that Autofill works only on a contiguous range. Once, you apply filter, the range becomes non-contiguous.

Now, here comes the trick -

1. Apply the filter.
2. Let's assume that first row is 3 and you wanted to fill it in column B.
3. Put following formula in B3 and drag down
=COUNTIF($B$1:B2,"<>"&"")

If you don't want to drag down -
3.1 Put the above formula in B3.
3.2 Select all the cells including B3.
3.2 Press F2
3.3 CTRL+Enter

Above steps will fill the filtered list with 1, 2, 3.....

------------------------------------------------------------------------------------------------------
Tips & Tricks 101 - Get Column Name for a Column Number
By eforexcel|Saturday, July 25th, 2015|Categories: Tips and Tricks|Tags: Address, Alphabets, Column, Names, Rows|1 Comment

Let's suppose, you have a number in A1 and you want to get the column Name for that.

Hence, if A1=1, you want "A"
Hence, if A1 =26, you want "Z"
Hence, if A1=27, you want "AA" and so on.

The formula to derive the column name would be be -

=SUBSTITUTE(ADDRESS(1,A1,4),1,"")

------------------------------------------------------------------------------------------------------
Tips & Tricks 100 - Get Sheet (tab) Name, Workbook Name and File Name through a formula
By eforexcel|Saturday, July 25th, 2015|Categories: Tips and Tricks|Tags: CELL, File Name, Sheet Name, Volatile, Workbook Name|0 Comments

There are many situation while working in Excel that you need to get the name of the sheet. (Note - For formulas to work, the workbook must be saved at least once)

The formula to retrieve file name would be -

=CELL("filename",$A$1)

The formula to retrieve the sheet name would be -

=REPLACE(CELL("filename",$A$1),1,FIND("]",CELL("filename",$A$1)),"")

Note - CELL is a volatile function, hence this will calculated for every change in the sheet.

The formula to retrieve workbook name would be -

=REPLACE(LEFT(CELL("filename",$A$1),FIND("]",CELL("filename",$A$1))-1),1,FIND("[",CELL("filename",$A$1)),"")

Note - CELL is a volatile function. Hence, the formulas would recalculate every time, the worksheet changes.