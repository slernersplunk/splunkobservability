#gets a list of login events
#change endTime and startTime to unix time of time window you need
curl \
    --request POST \
    --header "Content-Type: application/json" \
    --header "X-SF-Token: YOURTOKENHERE" \
    --data '{"query":"(sf_eventType:\"SessionLog\")","programToQuery":null,"limit":50,"offset":0,"endTime":1607018740603,"startTime":1604340340601,"orderBy":["-sf_timestamp"],"fields":["*"]}' \
    https://api.us1.signalfx.com/v2/event/find
