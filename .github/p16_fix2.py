#!/usr/bin/env python3
from pathlib import Path

P = Path('Vindex Chat-GPT/vindex_final_v51/bibliotheca/fenestrale_ii_purus.vindex')
t = P.read_text(encoding='utf-8')
a = t.index('FUNCTIO FV_TEXTUM_SCALA REDDENS NUMERUS.')
b = t.index('\nFUNCTIO FV_FUNDUM REDDENS NUMERUS.', a)
novum = '''FUNCTIO FV_TEXTUM_SCALA REDDENS NUMERUS.
    ACCIPIT x SICUT NUMERUS.
    ACCIPIT y SICUT NUMERUS.
    ACCIPIT textus SICUT TEXTUS.
    ACCIPIT color SICUT NUMERUS.
    ACCIPIT scala SICUT NUMERUS.
    SI scala < 1 TUNC scala = 1. FIN-SI.
    DECLARA forma SICUT NUMERUS VALENS CONTENTUM(50333784).
    SI forma == 0 TUNC REDDE 0. FIN-SI.
    DECLARA longitudo SICUT NUMERUS VALENS CONTENTUM(textus).
    DECLARA i SICUT NUMERUS VALENS 0.
    DUM i < longitudo PERFICE
        DECLARA littera SICUT NUMERUS VALENS OCTETUS_AB(textus + 8 + i).
        DECLARA py SICUT NUMERUS VALENS 0.
        DUM py < 8 PERFICE
            DECLARA bits SICUT NUMERUS VALENS OCTETUS_AB(forma + littera * 8 + py).
            DECLARA px SICUT NUMERUS VALENS 0.
            DUM px < 8 PERFICE
                SI (bits & (128 >> px)) != 0 TUNC
                    DECLARA sy SICUT NUMERUS VALENS 0.
                    DUM sy < scala PERFICE
                        DECLARA sx SICUT NUMERUS VALENS 0.
                        DUM sx < scala PERFICE
                            DECLARA f SICUT NUMERUS VALENS FV_PIXEL_COLOR(x + i * 8 * scala + px * scala + sx, y + py * scala + sy, color).
                            sx = sx + 1.
                        FIN-DUM.
                        sy = sy + 1.
                    FIN-DUM.
                FIN-SI.
                px = px + 1.
            FIN-DUM.
            py = py + 1.
        FIN-DUM.
        i = i + 1.
    FIN-DUM.
    REDDE 1.
FIN-FUNCTIO.'''
P.write_text(t[:a] + novum + t[b:], encoding='utf-8')
print('RECTE: textus scalaris per FV_PIXEL_COLOR viam probatam pingitur.')
