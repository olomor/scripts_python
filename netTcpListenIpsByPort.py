def getTcpListenIpsByPort(SearchPort):
    IpList = []
    for Line in [ l.strip() for l in open('/proc/net/tcp','r').readlines() ]:
        HexaLocalAddress = Line.split()[1]
        HexaRemoteAddress = Line.split()[2]
        if HexaRemoteAddress == '00000000:0000':
            HexaAddress, HexaPort = HexaLocalAddress.split(':')
            TcpPort = int(HexaPort,16)
            if TcpPort == SearchPort:
                IpList.append(''.join([ 
                    str(int(HexaAddress[6:8],16)), '.',
                    str(int(HexaAddress[4:6],16)), '.', 
                    str(int(HexaAddress[2:4],16)), '.', 
                    str(int(HexaAddress[0:2],16)),
                    ])
                )
    return IpList

