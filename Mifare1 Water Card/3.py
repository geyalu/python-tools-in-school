from smartcard.scard import *
import smartcard.util

hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)

assert hresult==SCARD_S_SUCCESS

hresult, readers = SCardListReaders(hcontext, [])

assert len(readers)>0

reader = readers[0]

hresult, hcard, dwActiveProtocol = SCardConnect(
    hcontext,
    reader,
    SCARD_SHARE_SHARED,
    SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)


def load_key(key_A):
    key = smartcard.util.toBytes(key_A)
    APDU=[0xFF,0x82,0x00,0x00,0x06]
    APDU=APDU+key
    response = SCardTransmit(hcard,dwActiveProtocol,APDU)
    #print smartcard.util.toHexString(response[1])
    if response[1][0]==144:
        print "-- Load Key Success --"
    else:
        return 0

def authenticate_block(block):
    APDU=[0xFF,0x86,0x00,0x00,0x05,0x01,0x00,0x3E,0x60,0x00]
    APDU[-3]=block
    response = SCardTransmit(hcard,dwActiveProtocol,APDU)
    if response[1][0]==144:
        print "-- Authenticate Block Success --"
    else:
        return 0


def read_data(block):
    APDU=[0xFF,0xB0,0x00,0x3E,0x0F]
    APDU[-2]=block
    response = SCardTransmit(hcard,dwActiveProtocol,APDU)
    #print smartcard.util.toHexString(response[1])
    if response[1][0]==144:
        print "-- Authenticate Block Success --"
        return response[1]
    else:
        return 0


def write_data(block,data):
    APDU=[0xFF,0xD6,0x00]
    APDU.append(block)
    APDU.append(0x10)
    APDU=APDU+data
    response = SCardTransmit(hcard,dwActiveProtocol,APDU)
    #print response
    #print smartcard.util.toHexString(response[1])
    if response[1][0]==144:
