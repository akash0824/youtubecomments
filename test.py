import youtubecomments as ytc

googleapikey = "AIzaSyBjgznNPIf6hZgQTWCBA0EpgM7SrRl8F8I"
videoid = "vbt_Lm2tXMY"
outputformat = "dataframe"

data = ytc.get_comments(googleapikey, videoid, outputformat)

data.to_csv("output.csv", index = False)
