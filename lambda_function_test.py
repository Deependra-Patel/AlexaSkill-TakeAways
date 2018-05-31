from lambda_function import lambda_handler

EXAMPLE_INTENT_REQUEST = {
    "version": "1.0",
    "session": {
        "new": True,
        "sessionId": "amzn1.echo-api.session.b3bdfb05-bf08-4006-a7e4-ab042252cd48",
        "application": {
            "applicationId": "amzn1.ask.skill.f818ca4e-9ad3-4e69-80e6-e7c46611e066"
        },
        "user": {
            "userId": "amzn1.ask.account.AGXI4A3JBZ2RPB46J6J25AEJO77UCLZRXJXZFX7HWZPDECAMTSPUPNEAAFG5CP2INNW44DCAGTMFGOJWC6U54JYP254UULRLVV24QQYJYMPKV5PLPQ7552VYMGQNEQJXHDCWND2Y47F3P3UEDH56K73S64Z7XDQJ35ZSKTWES2A5T6TQMDD6WQBGYA63W53FHP6MMLAK5NFAGCI",
        }
    },
    "context": {
        "AudioPlayer": {
            "playerActivity": "IDLE"
        },
        "Display": {},
        "System": {
            "application": {
                "applicationId": "amzn1.ask.skill.f818ca4e-9ad3-4e69-80e6-e7c46611e066"
            },
            "user": {
                "userId": "amzn1.ask.account.dfad",
            },
            "device": {
                "deviceId": "amzn1.ask.device.dsfa",
                "supportedInterfaces": {
                    "AudioPlayer": {},
                    "Display": {
                        "templateVersion": "1.0",
                        "markupVersion": "1.0"
                    }
                }
            },
            "apiEndpoint": "https://api.eu.amazonalexa.com",
            "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLmY4MThjYTRlLTlhZDMtNGU2OS04MGU2LWU3YzQ2NjExZTA2NiIsImV4cCI6MTUyNzcyMzgxNCwiaWF0IjoxNTI3NzIwMjE0LCJuYmYiOjE1Mjc3MjAyMTQsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjoiQXR6YXxJd0VCSUFBLXpMeXdBWjhuX3A2clZYZ2Z0TXJlRUE2dGZ1ai0xNTd6TFB0a0g5dXZYVnpGRFl0R2pCaWotdE1IeGtSMlczV3UzbG9Id3lKYVJISWZDOGRGelFDOU5KLUFTRnl5aHc2Z1JDZjVZa25sTk92WXhjWmdMVDhLTTVBTG8xUUlPVmpPMF81Tnd5aUd6RlBMTnBlN2JJTEhxY1liZzNjVXFRVUJiTk9FanhZSXRzTUFyTEhSU0dzMGgteHl3Rm9jOVJqZ1FQWjFKZG1BbWdUT1RjR1BKYjZfS3diUldCbkhtSjVveUYtQ3RmcEhlLTJ1NkMwZVJia1hmRFQ5WW9yLUstRTA3SGlzUHkxYXNMVmVWU2xjSk9aRHdFUFdtOTJ0Ry1BM1U0bEp0cE1Tc3pYcmZfbFJxYzRxY0lPSUwyUzdIcU51R2o3ZmJWNzZ0SVNzbEx4N2FuSEtXODdzRWJnWkoybjhIdDBWTkIxcVozV1htMzA4SmZmZnhsZURKRjcyeFVrdkpUQjhJOU1PanBIVXNRSW5FUmFXMFlsODNYQ0FIeWc5ejFCeXFvN1hNcDNoTXVaQ093cTV3TW1uLVRhZ3JCQ0JXVllEOHZNSkczcV9Udm9WUW9iRWJoRVJ4Z0lPS1oyS29XMjRsUkh1ZWU3LU5UaWpyMVlZRnNrRWFsTjYwNmZPVVNuZWxuNEItLXJ4M29XZUhFMjcxaVlUWXVjcEdWZ2cwYUIyWVY5TWdnIiwiZGV2aWNlSWQiOiJhbXpuMS5hc2suZGV2aWNlLkFHQUpHUUZRV0tONEsyU0tIR0ZFWVRXUFVKNTc0TTZaWVBCN1NDTFlQRDJVTUVVV1hZUEIzWkZPVUhBSEVKNU5BQlZMWFgzQU8zV0dPSkc1V01RVEYzUDVDSEI0M01YWEhVMktPRU8zVzNHNERPV0JQSkVBSVg3S0xWQlpDT1UyS0xURE81NEQzVU1JS1RBTFBWSUI3UlI2R0FWUSIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFHWEk0QTNKQloyUlBCNDZKNkoyNUFFSk83N1VDTFpSWEpYWkZYN0hXWlBERUNBTVRTUFVQTkVBQUZHNUNQMklOTlc0NERDQUdUTUZHT0pXQzZVNTRKWVAyNTRVVUxSTFZWMjRRUVlKWU1QS1Y1UExQUTc1NTJWWU1HUU5FUUpYSERDV05EMlk0N0YzUDNVRURINTZLNzNTNjRaN1hEUUozNVpTS1RXRVMyQTVUNlRRTURENldRQkdZQTYzVzUzRkhQNk1NTEFLNU5GQUdDSSJ9fQ.ZdshVmieflj7tMrVrvFuWHlM2CdcGp7FMb4aCMhon4RgOwJbVpzHbtKhudrHSmCi8r12sVxUdBY6O8uERQrgED5eZZNyqVIwzR8BLN1xTMEx9wMIGa58ZhC9yLOt0stUiYk7PTXrRiPBuj5R_lqMdW45HYndLqglqszPXPONr0EG47IpROpa1xmDRFXeJ2IMh5Fcgp_JBN-STyfMz6USXU7h6K_EQe-ZO-_DqGwaldJxTwT7fQ6rjei24z726QRD1uoHs4rbJ7CMX2S7RcVhhheqw8Z1_pfiJEGvkP0PysfMoXXzr9t_q1I4KavNzAKnRezXVfmBohaJuCPT6QA7hQ"
        }
    },
    "request": {
        "type": "IntentRequest",
        "requestId": "amzn1.echo-api.request.b6afcd21-20da-4073-b348-9aa8c1293c82",
        "timestamp": "2018-05-30T22:43:34Z",
        "locale": "en-GB",
        "intent": {
            "name": "getRandomNearby",
            "confirmationStatus": "NONE"
        }
    }
}


def test_without_permission():
    lambda_handler(EXAMPLE_INTENT_REQUEST, {})


if __name__ == '__main__':
    test_without_permission()
