#ifndef INSTRUCTIONS_H
    #define INSTRUCTIONS_H

    typedef struct mother_board_s mother_board_t;

    int NUL(mother_board_t *mother_board, void *dev);
    int ICX(mother_board_t *mother_board, void *dev);
    int ICY(mother_board_t *mother_board, void *dev);
    int ADX(mother_board_t *mother_board, void *dev);
    int ADY(mother_board_t *mother_board, void *dev);
    int SUX(mother_board_t *mother_board, void *dev);
    int IDN(mother_board_t *mother_board, void *dev);
    int SUY(mother_board_t *mother_board, void *dev);
    int MUX(mother_board_t *mother_board, void *dev);
    int MUY(mother_board_t *mother_board, void *dev);
    int DIX(mother_board_t *mother_board, void *dev);
    int DIY(mother_board_t *mother_board, void *dev);
    int MOX(mother_board_t *mother_board, void *dev);
    int MOY(mother_board_t *mother_board, void *dev);
    int TVF(mother_board_t *mother_board, void *dev);
    int END(mother_board_t *mother_board, void *dev);
    int TVX(mother_board_t *mother_board, void *dev);
    int TVY(mother_board_t *mother_board, void *dev);
    int PPX(mother_board_t *mother_board, void *dev);
    int PPY(mother_board_t *mother_board, void *dev);
    int MPX(mother_board_t *mother_board, void *dev);
    int MPY(mother_board_t *mother_board, void *dev);
    int DMX(mother_board_t *mother_board, void *dev);
    int DMY(mother_board_t *mother_board, void *dev);
    int DPX(mother_board_t *mother_board, void *dev);
    int DPY(mother_board_t *mother_board, void *dev);
    int XVY(mother_board_t *mother_board, void *dev);
    int YVX(mother_board_t *mother_board, void *dev);
    int XVT(mother_board_t *mother_board, void *dev);
    int YVT(mother_board_t *mother_board, void *dev);
    int XVF(mother_board_t *mother_board, void *dev);
    int YVF(mother_board_t *mother_board, void *dev);
    int MVX(mother_board_t *mother_board, void *dev);
    int MVY(mother_board_t *mother_board, void *dev);
    int RDM(mother_board_t *mother_board, void *dev);
    int TMX(mother_board_t *mother_board, void *dev);
    int TMY(mother_board_t *mother_board, void *dev);
    int ANX(mother_board_t *mother_board, void *dev);
    int ANY(mother_board_t *mother_board, void *dev);
    int ORX(mother_board_t *mother_board, void *dev);
    int ORY(mother_board_t *mother_board, void *dev);
    int XOX(mother_board_t *mother_board, void *dev);
    int XOY(mother_board_t *mother_board, void *dev);
    int LSX(mother_board_t *mother_board, void *dev);
    int LSY(mother_board_t *mother_board, void *dev);
    int RSX(mother_board_t *mother_board, void *dev);
    int RSY(mother_board_t *mother_board, void *dev);
    int EQX(mother_board_t *mother_board, void *dev);
    int EQY(mother_board_t *mother_board, void *dev);
    int NQX(mother_board_t *mother_board, void *dev);
    int NQY(mother_board_t *mother_board, void *dev);
    int SPX(mother_board_t *mother_board, void *dev);
    int SPY(mother_board_t *mother_board, void *dev);
    int INX(mother_board_t *mother_board, void *dev);
    int INY(mother_board_t *mother_board, void *dev);
    int IEX(mother_board_t *mother_board, void *dev);
    int IEY(mother_board_t *mother_board, void *dev);
    int SEX(mother_board_t *mother_board, void *dev);
    int SEY(mother_board_t *mother_board, void *dev);
    int NOX(mother_board_t *mother_board, void *dev);
    int NOY(mother_board_t *mother_board, void *dev);
    int CNE(mother_board_t *mother_board, void *dev);
    int HALT(mother_board_t *mother_board, void *dev);
    int XPP(mother_board_t *mother_board, void *dev);
    int YPP(mother_board_t *mother_board, void *dev);
    int SWX(mother_board_t *mother_board, void *dev);
    int SWY(mother_board_t *mother_board, void *dev);
    int REX(mother_board_t *mother_board, void *dev);
    int REY(mother_board_t *mother_board, void *dev);
    int XMP(mother_board_t *mother_board, void *dev);
    int YMP(mother_board_t *mother_board, void *dev);
    int STX(mother_board_t *mother_board, void *dev);
    int STY(mother_board_t *mother_board, void *dev);
    int LOG(mother_board_t *mother_board, void *dev);

#endif /* INSTRUCTIONS_H */
