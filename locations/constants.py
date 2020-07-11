from .items import *

INVENTORY_MAP = {
    SWORD: "01",
    BOMB: "02",
    POWER_BRACELET: "03",
    SHIELD: "04",
    BOW: "05",
    HOOKSHOT: "06",
    MAGIC_ROD: "07",
    PEGASUS_BOOTS: "08",
    OCARINA: "09",
    FEATHER: "0A",
    SHOVEL: "0B",
    MAGIC_POWDER: "0C",
    BOOMERANG: "0D",
    TOADSTOOL: "0E",
}
INVENTORY_ICON = {
    SWORD: "8415",
    BOMB: "8015",
    POWER_BRACELET: "8215",
    SHIELD: "8615",
    BOW: "8814",
    HOOKSHOT: "8A14",
    MAGIC_ROD: "8C14",
    PEGASUS_BOOTS: "9816",
    OCARINA: "9014",
    FEATHER: "9216",
    SHOVEL: "9617",
    MAGIC_POWDER: "8E14",
    BOOMERANG: "241C",

    FLIPPERS: "9415",
    SLIME_KEY: "4E1C",
    TAIL_KEY: "301C",
    ANGLER_KEY: "321C",
    FACE_KEY: "341C",
    BIRD_KEY: "361C",
    GOLD_LEAF: "3A1C",

    RUPEES_50: "A615",
    RUPEES_20: "3819",
    RUPEES_100: "3818",
    RUPEES_200: "381A",
    RUPEES_500: "381A",
    SEASHELL: "9E14",
}
INVENTORY_NAME = {
    SWORD: b"Sword",
    BOMB: b"Bombs",
    POWER_BRACELET: b"Power Bracelet",
    SHIELD: b"Shield",
    BOW: b"Bow",
    HOOKSHOT: b"Hookshot",
    MAGIC_ROD: b"Magic Rod",
    PEGASUS_BOOTS: b"Pegasus Boots",
    OCARINA: b"Ocarina",
    FEATHER: b"Roc's Feather",
    SHOVEL: b"Shovel",
    MAGIC_POWDER: b"Magic Powder",
    BOOMERANG: b"Boomerang",

    FLIPPERS: b"Flippers",
    SLIME_KEY: b"Slime key",
    TAIL_KEY: b"Tail key",
    ANGLER_KEY: b"Angler key",
    FACE_KEY: b"Face key",
    BIRD_KEY: b"Bird key",
    GOLD_LEAF: b"Golden leaf",

    RUPEES_50: b"50 Rupees",
    RUPEES_20: b"20 Rupees",
    RUPEES_100: b"100 Rupees",
    RUPEES_200: b"200 Rupees",
    RUPEES_500: b"500 Rupees",
    SEASHELL: b"Secret Seashell",

    KEY1: b"Key for Tail Cave",
    KEY2: b"Key for Bottle Grotto",
    KEY3: b"Key for Key Cavern",
    KEY4: b"Key for Angler's Tunnel",
    KEY5: b"Key for Catfish's Maw",
    KEY6: b"Key for Face Shrine",
    KEY7: b"Key for Eagle's Tower",
    KEY8: b"Key for Turtle Rock",
    KEY9: b"Key for Color Dungeon",

    MAP1: b"Map for Tail Cave",
    MAP2: b"Map for Bottle Grotto",
    MAP3: b"Map for Map Cavern",
    MAP4: b"Map for Angler's Tunnel",
    MAP5: b"Map for Catfish's Maw",
    MAP6: b"Map for Face Shrine",
    MAP7: b"Map for Eagle's Tower",
    MAP8: b"Map for Turtle Rock",
    MAP9: b"Map for Color Dungeon",

    COMPASS1: b"Compass for Tail Cave",
    COMPASS2: b"Compass for Bottle Grotto",
    COMPASS3: b"Compass for Compass Cavern",
    COMPASS4: b"Compass for Angler's Tunnel",
    COMPASS5: b"Compass for Catfish's Maw",
    COMPASS6: b"Compass for Face Shrine",
    COMPASS7: b"Compass for Eagle's Tower",
    COMPASS8: b"Compass for Turtle Rock",
    COMPASS9: b"Compass for Color Dungeon",

    STONE_BEAK1: b"Stone Beak for Tail Cave",
    STONE_BEAK2: b"Stone Beak for Bottle Grotto",
    STONE_BEAK3: b"Stone Beak for Stone Beak Cavern",
    STONE_BEAK4: b"Stone Beak for Angler's Tunnel",
    STONE_BEAK5: b"Stone Beak for Catfish's Maw",
    STONE_BEAK6: b"Stone Beak for Face Shrine",
    STONE_BEAK7: b"Stone Beak for Eagle's Tower",
    STONE_BEAK8: b"Stone Beak for Turtle Rock",
    STONE_BEAK9: b"Stone Beak for Color Dungeon",

    NIGHTMARE_KEY1: b"Nightmare Key for Tail Cave",
    NIGHTMARE_KEY2: b"Nightmare Key for Bottle Grotto",
    NIGHTMARE_KEY3: b"Nightmare Key for Nightmare Key Cavern",
    NIGHTMARE_KEY4: b"Nightmare Key for Angler's Tunnel",
    NIGHTMARE_KEY5: b"Nightmare Key for Catfish's Maw",
    NIGHTMARE_KEY6: b"Nightmare Key for Face Shrine",
    NIGHTMARE_KEY7: b"Nightmare Key for Eagle's Tower",
    NIGHTMARE_KEY8: b"Nightmare Key for Turtle Rock",
    NIGHTMARE_KEY9: b"Nightmare Key for Color Dungeon",

    HEART_PIECE: b"Piece of Heart",
    BOWWOW: b"Bowwow",
    ARROWS_10: b"10 Arrows",
    SINGLE_ARROW: b"Single Arrow",

    MAX_POWDER_UPGRADE: b"Powder upgrade",
    MAX_BOMBS_UPGRADE: b"Bombs upgrade",
    MAX_ARROWS_UPGRADE: b"Arrows upgrade",

    RED_TUNIC: b"Red Tunic",
    BLUE_TUNIC: b"Blue Tunic",

    HEART_CONTAINER: b"Heart Container",
    BAD_HEART_CONTAINER: b"Anti-Heart Container",

    TOADSTOOL: b"Toadstool",
}
CHEST_ITEMS = {
    POWER_BRACELET: 0x00,
    SHIELD: 0x01,
    BOW: 0x02,
    HOOKSHOT: 0x03,
    MAGIC_ROD: 0x04,
    PEGASUS_BOOTS: 0x05,
    OCARINA: 0x06,
    FEATHER: 0x07, SHOVEL: 0x08, MAGIC_POWDER: 0x09, BOMB: 0x0A, SWORD: 0x0B, FLIPPERS: 0x0C,
    MAGNIFYING_LENS: 0x0D, MEDICINE: 0x10,
    TAIL_KEY: 0x11, ANGLER_KEY: 0x12, FACE_KEY: 0x13, BIRD_KEY: 0x14, GOLD_LEAF: 0x15,
    RUPEES_50: 0x1B, RUPEES_20: 0x1C, RUPEES_100: 0x1D, RUPEES_200: 0x1E, RUPEES_500: 0x1F,
    SEASHELL: 0x20, MESSAGE: 0x21, GEL: 0x22,
    MAP: 0x16, COMPASS: 0x17, STONE_BEAK: 0x18, NIGHTMARE_KEY: 0x19, KEY: 0x1A,

    BOOMERANG: 0x0E,
    SLIME_KEY: 0x0F,

    KEY1: 0x23,
    KEY2: 0x24,
    KEY3: 0x25,
    KEY4: 0x26,
    KEY5: 0x27,
    KEY6: 0x28,
    KEY7: 0x29,
    KEY8: 0x2A,
    KEY9: 0x2B,

    MAP1: 0x2C,
    MAP2: 0x2D,
    MAP3: 0x2E,
    MAP4: 0x2F,
    MAP5: 0x30,
    MAP6: 0x31,
    MAP7: 0x32,
    MAP8: 0x33,
    MAP9: 0x34,

    COMPASS1: 0x35,
    COMPASS2: 0x36,
    COMPASS3: 0x37,
    COMPASS4: 0x38,
    COMPASS5: 0x39,
    COMPASS6: 0x3A,
    COMPASS7: 0x3B,
    COMPASS8: 0x3C,
    COMPASS9: 0x3D,

    STONE_BEAK1: 0x3E,
    STONE_BEAK2: 0x3F,
    STONE_BEAK3: 0x40,
    STONE_BEAK4: 0x41,
    STONE_BEAK5: 0x42,
    STONE_BEAK6: 0x43,
    STONE_BEAK7: 0x44,
    STONE_BEAK8: 0x45,
    STONE_BEAK9: 0x46,

    NIGHTMARE_KEY1: 0x47,
    NIGHTMARE_KEY2: 0x48,
    NIGHTMARE_KEY3: 0x49,
    NIGHTMARE_KEY4: 0x4A,
    NIGHTMARE_KEY5: 0x4B,
    NIGHTMARE_KEY6: 0x4C,
    NIGHTMARE_KEY7: 0x4D,
    NIGHTMARE_KEY8: 0x4E,
    NIGHTMARE_KEY9: 0x4F,

    TOADSTOOL: 0x50,

    HEART_PIECE: 0x80,
    BOWWOW: 0x81,
    ARROWS_10: 0x82,
    SINGLE_ARROW: 0x83,

    MAX_POWDER_UPGRADE: 0x84,
    MAX_BOMBS_UPGRADE: 0x85,
    MAX_ARROWS_UPGRADE: 0x86,

    RED_TUNIC: 0x87,
    BLUE_TUNIC: 0x88,
    HEART_CONTAINER: 0x89,
    BAD_HEART_CONTAINER: 0x8A,

    SONG1: 0x8B,
    SONG2: 0x8C,
    SONG3: 0x8D,
}
