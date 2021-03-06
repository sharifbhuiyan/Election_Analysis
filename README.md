## **<h1 align="center"> Election  Audit Analysis**




  ## Overview of Election Audit: 
<p align="justify">Election audit analysis was submitted to the election commission as per their requirements. Commission had the following additional requirements with the details candidate results. <p>
  
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

<p align="justify">Two technical analysis were performed to complete the Election audit analysis. The coding for the Election results was conducted by Python command line with VS code editor. Results also saved to a Text File. <p>

  Election audit Analysis Python.py file link -  [ Election  Audit Analysis](https://github.com/sharifbhuiyan/Election_Analysis/blob/main/PyPoll_Challenge.py)  

  
- Resources :
  - Data source : election_results.txt
  - Software : Python 3.10.4, Visual Studio Code editor 1.66.0


  
  
  

  
  
 ## Election-Audit Results: 
  
<p align="justify"> The election-audit analysis was furnished for three candidates with three counties. The Candidates were Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane  and the counties were Jefferson, Denver, Arapahoe. The snap shot of Final result in commandline and txt file was : <p>
  
<p align="center">
  <img width="500" src=https://github.com/sharifbhuiyan/Election_Analysis/blob/main/Resources/Anlysis_3.png
</p>
  
  
  Command for Save the winning candidate's summary to the text file :
  ```ruby
    
    txt_file.write(winning_candidate_summary)

```
  
    
 Command for print the winning candidate to terminal :

  
 ```ruby
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
  ```
  
  
 ### Election-Audit analysis outcomes were :

- Total  369,711 votes were cast in this congressional election.

- The number of votes and the percentage of total votes casted for each county was :
 
 <p align="center">
   
| 	County  | % of casting vote  | Casting vote |
| :------------ |:---------------:| -----:|
| Jefferson      | 10.5% | 38,855 |
| Denver      | 82.8%        |   306,055 |
| Arapahoe | 6.7%        |    24,801 |

</p>
   
   
- The county, Denver had the largest number of votes, 306,055.

- The number of votes and the percentage of the total votes each candidate received :

| 	Candate  | Number of received votes  | % of received vote |
| :------------ |:---------------:| -----:|
| Charles Casper Stockham      | 85,213 | 323.0% |
| Diana DeGette      | 272,892        |   73.8% |
| Raymon Anthony Doane | 11,606        |    3.1% |
  
- Diana DeGette won the election. The number of received votes was 272,892 and percentage of the total votes was  73.8%.
  
  
 

    
    
    
    
## Election-Audit Summary:
  <p align="justify">Though this analysis was for only three candidates and three counties, however if election commission wants to use it for other election, it can be applied for any election. Only few modifications are needed for that.
<p>
  
<p align="justify">Suppose for city election, need to change the all county tracking code. Like : <p>

- Have to remove the code for tracking the largest county and county voter turnout.
```ruby   
county_name = ""
county_voting = 0
```
  
  - Have to remove the code for printing the largest turnout county.
  
  ```ruby   
    winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {c_winning_county}\n"
    # f"Winning Vote Count: {c_winning_count:,}\n"
    # f"Winning Percentage: {c_winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_county_summary)
```
