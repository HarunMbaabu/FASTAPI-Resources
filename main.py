from fastapi import FastAPI 


app = FastAPI()


@app.get("/")
async def Index():
	return {
	         "Name": "Harun Mbaabu Mwenda",
	         "Career": "Software Engineer & Data Scientist",
	         "Country": "Kenya",
	         "Age": "24",
	         "Twitter": "https://twitter.com/HarunMbaabu"
	        } 
