# file_search

file search module will help you to find out the location of any file using a string.

Example -
-------------------------------------------------------
import file_search

file_search.set_root('D:\\')      
files = file_search.searchFile('library management')

--------------------------------------------------------

in files, searchFile() function will return a list of filenames with their respective locations.
in above example, we're setting root as 'D:\\' , so the searching of file will be start from D:\\.
then we're passing 'library' inside the function, so it will return all the files that are having 'library' and 'management' keyword in its name.




