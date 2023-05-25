# add to /seek/share/zeek/site/local.zeek

@load tuning/json-logs
redef LogAscii::json_timestamps = JSON::TS_ISO8601;
redef LogAscii::unset_field = "-";
redef LogAscii::use_json = T;
redef LogAscii::gzip_level = 0;
