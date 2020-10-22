curl \
  --request POST \
  --header "X-SF-TOKEN: YOURTOKENHERE" \
  --header "Content-Type: application/json" \
  --data \
 '[{ 
      "category":"USER_DEFINED" 
   }, 
   { 
      "eventType":"Jenkins Build", 
      "properties":{
         "application":"UserRegistration",
         "function":"Deploy", 
         "version":"1.0"
      } 
   }]' \
https://ingest.YOURREALMHERE.signalfx.com/v2/event
