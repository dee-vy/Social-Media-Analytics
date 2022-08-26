Data:
<ul>
<li>Raw JSON data:
    <br /> CodeTesting -> json_to_csv -> json_files</li>
<li>A combined CSV of all the Irish users' data is stored at:
    <br /> CodeTesting -> json_to_csv -> csv_files  -> irish -> All_combined_irish.csv
    <br /> CodeTesting -> json_to_csv -> csv_files  -> irish -> All_combined_irish_stopwords_removed.csv</li>
<li>After pre-processing and splitting each entry of the CSVs into separate documents, the folders are:
<br /> CodeTesting -> json_to_csv -> All_combined_irish_docs
<br /> CodeTesting -> json_to_csv -> All_combined_irish_stopwords_removed_docs
</li>
</ul>


Structure of the code:
<ol>
<li> Using the Snscrape tool, I have fetched the data in JSON format at the location: 
     <br /> json_to_csv/json_files </li>
<li> "main.py" to take the Irish user tweets and convert those into CSV. Combined CSV stored at:
      <br /> json_to_csv/csv_files/irish/All_combined_irish.csv </li>
<li> "nltk_stopwords_removal.py" to remove stop words. Combined CSV stored at: 
      <br /> json_to_csv/csv_files/irish/All_combined_irish_stopwords_removed.csv </li>
<li> 'Csv_to_document.py' then pre-processes from the combined CSVs and stores each entry of the data (tweets) into a separate document stored at:
      <br /> json_to_csv/irish/All_combined_irish_docs
      <br /> json_to_csv/irish/All_combined_irish_stopwords_removed_docs</li>
<li> 'textmatrix' and semantic space created using 'LSA.R' </li>
<li> Tokens are split up into five topics in "LSA.R" and stored in:
     <br /> json_to_csv/Matrix_Data/tokenFile2.txt</li>
<li> "Emotion_Wordtype.py" to fetch data from "tokenFile2.txt" and add two more categories for emotion and word types against each topic field.
      <br /> New file stored here: json_to_csv/Matrix_Data/tokenFile2_em_wtype.csv</li>
<li> Using 'tokenFile2_em_wtype.csv', various tests and plots have been implemented in "LSA.R'.</li>
</ol>


Note:
"setwd" in LSA.R works on an absolute path. Hence, it needs to be updated based on personal machines.
