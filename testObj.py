customer_name = 'local'
temp_file_name = "temp_" + customer_name + ".env"

config_data = {
    "NEW_RELIC_ENABLED": "true",
    "NEW_RELIC_LOG_LEVEL": "debug"
}


with open(temp_file_name, 'a') as file:
    # todo: revert to defaults if no configuration found in the DB
    NEW_RELIC_ENABLED = config_data["NEW_RELIC_ENABLED"] if ("NEW_RELIC_ENABLED" in config_data) else "true"
    NEW_RELIC_TRACER_ENABLED = config_data["NEW_RELIC_TRACER_ENABLED"] if ("NEW_RELIC_TRACER_ENABLED" in config_data) else "true"
    NEW_RELIC_LOG_LEVEL = config_data["NEW_RELIC_LOG_LEVEL"] if ("NEW_RELIC_LOG_LEVEL" in config_data) else "info"

    file.write("NEW_RELIC_ENABLED=" + NEW_RELIC_ENABLED + "\n")
    file.write("NEW_RELIC_TRACER_ENABLED=" + NEW_RELIC_TRACER_ENABLED + "\n")
    file.write("NEW_RELIC_LOG_LEVEL=" + NEW_RELIC_LOG_LEVEL + "\n")
