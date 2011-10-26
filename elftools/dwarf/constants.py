#-------------------------------------------------------------------------------
# elftools: dwarf/constants.py
#
# Constants and flags
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------------

# Inline codes
#
DW_INL_not_inlined=0
DW_INL_inlined=1
DW_INL_declared_not_inlined=2
DW_INL_declared_inlined=3


# Source languages
#
DW_LANG_C89=0x0001
DW_LANG_C=0x0002
DW_LANG_Ada83=0x0003
DW_LANG_C_plus_plus=0x0004
DW_LANG_Cobol74=0x0005
DW_LANG_Cobol85=0x0006
DW_LANG_Fortran77=0x0007
DW_LANG_Fortran90=0x0008
DW_LANG_Pascal83=0x0009
DW_LANG_Modula2=0x000a
DW_LANG_Java=0x000b
DW_LANG_C99=0x000c
DW_LANG_Ada95=0x000d
DW_LANG_Fortran95=0x000e
DW_LANG_PLI=0x000f
DW_LANG_ObjC=0x0010
DW_LANG_ObjC_plus_plus=0x0011
DW_LANG_UPC=0x0012
DW_LANG_D=0x0013
DW_LANG_Python=0x0014
DW_LANG_Mips_Assembler=0x8001
DW_LANG_Upc=0x8765
DW_LANG_HP_Bliss=0x8003
DW_LANG_HP_Basic91=0x8004
DW_LANG_HP_Pascal91=0x8005
DW_LANG_HP_IMacro=0x8006
DW_LANG_HP_Assembler=0x8007


# Encoding
#
DW_ATE_void=0x0
DW_ATE_address=0x1
DW_ATE_boolean=0x2
DW_ATE_complex_float=0x3
DW_ATE_float=0x4
DW_ATE_signed=0x5
DW_ATE_signed_char=0x6
DW_ATE_unsigned=0x7
DW_ATE_unsigned_char=0x8
DW_ATE_imaginary_float=0x9
DW_ATE_packed_decimal=0xa
DW_ATE_numeric_string=0xb
DW_ATE_edited=0xc
DW_ATE_signed_fixed=0xd
DW_ATE_unsigned_fixed=0xe
DW_ATE_decimal_float=0xf
DW_ATE_UTF=0x10
DW_ATE_lo_user=0x80
DW_ATE_hi_user=0xff
DW_ATE_HP_float80=0x80
DW_ATE_HP_complex_float80=0x81
DW_ATE_HP_float128=0x82
DW_ATE_HP_complex_float128=0x83
DW_ATE_HP_floathpintel=0x84
DW_ATE_HP_imaginary_float80=0x85
DW_ATE_HP_imaginary_float128=0x86

