#ifndef __ntoh_h__
#define __ntoh_h__
#include <stdint.h>
#include <xclib.h>

#define NTOH_U16_ALIGNED(x) ((uint16_t) (byterev((x)[0]) >> 16))

#endif