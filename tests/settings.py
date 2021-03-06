from PyKCS11 import (CKG_MGF1_SHA256, CKM_SHA256, CKM_SHA256_RSA_PKCS_PSS,
                     CKM_SHA512, RSA_PSS_Mechanism)

MOCK_PYKCS11 = True  # Set to False to test it with real PyKCS11Lib and smart card

VALID_KEY_ID = (0x01,)
WRONG_KEY_ID = (0x20,)

VALID_PIN = '123456'
WRONG_PIN = 'xxxxxx'

VALID_MECH = RSA_PSS_Mechanism(CKM_SHA256_RSA_PKCS_PSS, CKM_SHA256, CKG_MGF1_SHA256, 32)
WRONG_MECH = RSA_PSS_Mechanism(CKM_SHA256_RSA_PKCS_PSS, CKM_SHA512, CKG_MGF1_SHA256, 32)
