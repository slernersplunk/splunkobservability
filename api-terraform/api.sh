curl \
    --request POST \
    --header "Content-Type: text/plain" \
    --header "X-SF-Token: YOURTOKENHERE" \
    --data "data(\"cpu.utilization\").mean().publish()" \
    https://api.YOURREALMHERE.signalfx.com/v2/signalflow/execute
