#!/bin/sh

FILENAME="$1"
TIMEOUT="$2"

geth --dev --http --http.api eth,web3,personal,net &
sleep 2
export WEB3_PROVIDER_URI="http://127.0.0.1:8545"

if [ "$TIMEOUT" -eq 0 ]; then
    cat "$FILENAME" | pakala -
else
    # TO1 = TIMEOUT * 80%
    # TO2 = TIMEOUT * 17%
    TO1=$(( TIMEOUT*8/10 ))
    TO2=$(( TIMEOUT*17/100 ))
    cat "$FILENAME" | pakala - --exec-timeout ${TO1} --analysis-timeout ${TO2}
fi
