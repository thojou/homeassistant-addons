#!/usr/bin/env bashio

bashio::log.info '======================================'
bashio::log.info '====      Start Flare DNS         ===='
bashio::log.info '======================================'

while true; do
    bashio::log.info "Run Flare DNS Job"
    python3 /dyndns.py
    bashio::log.info "Completed Flare DNS. Sleep for ${INTERVAL}" 

    sleep "${INTERVAL}"
done
