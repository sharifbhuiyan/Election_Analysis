## **<h1 align="center"> Election  Audit Analysis**




  ## 1. Overview of Election Audit: 
<p align="justify">Election audit analysis was submitted to the election commission as per their requirement. Commission had the following requirement. <p>
  
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

<p align="justify">Two technical analysis were performed to complete the Election audit analysis. The coding for the Election results was conducted by Python command line with VS code editor. Results also saved to a Text File. Election audit Analysis Python.py file is available in download link as below <p>

  - [ Election  Audit Analysis](https://github.com/sharifbhuiyan/stock-analysis/blob/main/VBA_Challenge.xlsm)  

- Resources :
            Data source : election_results.txt
            Software : Python 3.10.4, 
                      Visual Studio Code editor 1.66.0


  
  
  ## 2. Election-Audit Results: 
  
<p align="justify"> The election-audit analysis was furnished for three candidates with three counties. The Candidates were Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane  and the counties were Jefferson, Denver, Arapahoe. The snap shot of Final result in commandline and txt file was : <p>
  
  <p align="center">
  <img width="500" src=https://github.com/sharifbhuiyan/Election_Analysis/blob/main/Resources/Anlysis_3.png
</p>
  
  
 Election-Audit analysis outcomes were :

- Total  369,711 votes were cast in this congressional election.

- The number of votes and the percentage of total votes casted for each county was :
 

| 	County  | % of casting vote  | Casting vote |
| :------------ |:---------------:| -----:|
| Jefferson      | 10.5% | 38,855 |
| Denver      | 82.8%        |   306,055 |
| Arapahoe | 6.7%        |    24,801 |
  
- The county, Denver had the largest number of votes.

- The number of votes and the percentage of the total votes each candidate received :

| 	Candate  | Number of received votes  | % of received vote |
| :------------ |:---------------:| -----:|
| Charles Casper Stockham      | 85,213 | 323.0% |
| Diana DeGette      | 272,892        |   73.8% |
| Raymon Anthony Doane | 11,606        |    3.1% |
  
- Diana DeGette won the election. The number of votes that he received were 272,892 and percentage of the total votes was  73.8%.
  
  
 # Print the winning candidate (to terminal)
 ```ruby
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
 ```

    
```ruby
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

    
    
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
 ```
    
```ruby
    # 6f: Write an if statement to determine the winning county and get its vote count.
        if (c_votes > c_winning_count) and (c_vote_percentage > c_winning_percentage):
            c_winning_count = c_votes
            c_winning_county= county_name
            c_winning_percentage = c_vote_percentage 
```    
    
    
    
## 3. Summary:
  <p align="justify">Though programmers and software developers refactor the code to improve the design, structure and implementation of software, besides advantages, it has disadvantages also.<p>
  

