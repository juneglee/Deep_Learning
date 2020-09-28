from text import cmudict


_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_punctuation = '!\'(),.:;?' # 특수문자
_space = ' ' # 공백
_special = '-' # 
_pad = ' ' #텍스트들의 길이를 맞추기 위해서 사용

_arpabet = ['@' + s for s in cmudict.valid_symbols] # cmudict 안의 내용을 @을 표시해서 사용
# _kor_letter = None # 한국어를 처리할 때 letter를 변경한다.

symbols = [_pad] + [_special] + list(_punctuation) + [_space] + list(_letters) + _arpabet

_JAMO_LEADS = "".join([chr(_) for _ in range(0x1100, 0x1113)])
_JAMO_VOWELS = "".join([chr(_) for _ in range(0x1161, 0x1176)])
_JAMO_TATLS = "".join([chr(_) for _ in range(0x11A8, 0x11C3)])
_VAILD_JAMO = [jamo for jamo in _JAMO_LEADS + _JAMO_VOWELS + _JAMO_TATLS]

korean_symbols = [_pad] + [_special] + list(_punctuation) + [_space] + _VAILD_JAMO

if __name__ == '__main__':
    # print(symbols) # 음성으로 사용하기 위해서는 숫자의 형태로 사용할 수 있어야 하며, 위의 결과로 숫자화를 준비한다.
    # print(len(symbols))
    #
    # symbols_to_id = {s: i for i, s in enumerate(symbols)} # 숫자화, 딕셔너리로 표현 <text, audio >
    #
    # print(symbols_to_id) # 위에서 처리한 결과를 enumerate을 통해서 각각의 0부터 숫자로 만들어 준다.
    # print(len(symbols_to_id))

    print(korean_symbols) # 음성으로 사용하기 위해서는 숫자의 형태로 사용할 수 있어야 하며, 위의 결과로 숫자화를 준비한다.
    print(len(korean_symbols))

    symbols_to_id = {s: i for i, s in enumerate(korean_symbols)}
    
    text = '안녕하세요 3 분반'

    from jamo import hangul_to_jamo

    h2j = "".join(hangul_to_jamo(text)) # 초성 중성 종성으로 분류되어있는 상태

    print([symbols_to_id[jamo] for jamo in h2j])
    # print([symbols_to_id[jamo] for jamo in text]) # error
    print([jamo for jamo in h2j])