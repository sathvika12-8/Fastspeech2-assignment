""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. """

from text import cmudict, pinyin

_pad = "_"
_punctuation = "!'(),.:;? "
_special = "-"
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_silences = ["@sp", "@spn", "@sil"]


MFA_TELUGU_PHONES = ["@'a", "@'a:", "@'aI", "@'aU", "@'e", "@'e:", "@'i", "@'i:", "@'o", "@'o:", "@'u", "@'u:", '@,a', '@,a:', '@,aI', '@,aU', '@,e', '@,e:', '@,i', '@,i:', '@,o', '@,o:', '@,u', '@,u:', '@;', '@J', '@J#', '@N', '@S;', '@a', '@a:', '@aI', '@aU', '@b', '@b#', '@c', '@c#', '@d', '@d#', '@d.', '@d.#', '@e', '@e:', '@g', '@g#', '@h', '@i', '@i:', '@j', '@k', '@k#', '@l', '@l.', '@m', '@n', '@n.', '@n^', '@o', '@o:', '@p', '@p#', '@r', '@s', '@s.', '@t', '@t#', '@t.', '@t.#', '@u', '@u:', '@v#']

MFA_SVARAH_PHONES = ['@a', '@aj', '@aw', '@aː', '@b', '@bʲ', '@c', '@cʰ', '@cʷ', '@d', '@dʒ', '@dʲ', '@d̪', '@e', '@ej', '@eː', '@f', '@fʲ', '@h', '@i', '@iː', '@j', '@k', '@kʰ', '@kʷ', '@l', '@m', '@mʲ', '@m̩', '@n', '@o', '@ow', '@oː', '@p', '@pʰ', '@pʲ', '@s', '@spn', '@t', '@tʃ', '@tʰ', '@tʲ', '@tʷ', '@t̪', '@u', '@uː', '@v', '@vʲ', '@w', '@z', '@æ', '@ç', '@ð', '@ŋ', '@ɐ', '@ɑ', '@ɑː', '@ɒ', '@ɒː', '@ɔ', '@ɔj', '@ɖ', '@ə', '@əw', '@ɚ', '@ɛ', '@ɛː', '@ɜ', '@ɜː', '@ɝ', '@ɟ', '@ɟʷ', '@ɡ', '@ɡʷ', '@ɪ', '@ɫ', '@ɲ', '@ɹ', '@ɾ', '@ʃ', '@ʈ', '@ʈʲ', '@ʉ', '@ʉː', '@ʊ', '@ʋ', '@ʎ', '@ʒ', '@θ']


# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ["@" + s for s in cmudict.valid_symbols]
_pinyin = ["@" + s for s in pinyin.valid_symbols]

# Export all symbols:
symbols = (
    [_pad]
    + list(_special)
    + list(_punctuation)
    + list(_letters)
    + _arpabet
    + _pinyin
    + MFA_SVARAH_PHONES
    + MFA_TELUGU_PHONES
    + _silences
)
