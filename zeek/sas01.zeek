# http://ce.sc.edu/cyberinfra/workshops/workshop_2020/zeek_labs/Lab%206%20-%20Introduction%20to%20Zeek%20Scripting.pdf

event zeek_init(){
    print("Start");
}

event  udp_request(u: connection){
    print "---------------------------------------------";
    print "UDP reques: ", u;
}

event  tcp_packet(u: connection, is_orig: bool, flags: string, seq: count, ack: count, len: count, payload: string){
    print "--------------------------------------------------------------------------------------------------------";
    print "TCP reques: ", len;
}


event zeek_done(){
    print("Ennnd");
}
