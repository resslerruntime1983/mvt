# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2022 Claudio Guarnieri.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

IPHONE_MODELS = [
    {"identifier": "iPhone4,1", "description": "iPhone 4S"},
    {"identifier": "iPhone5,1", "description": "iPhone 5"},
    {"identifier": "iPhone5,2", "description": "iPhone 5"},
    {"identifier": "iPhone5,3", "description": "iPhone 5c"},
    {"identifier": "iPhone5,4", "description": "iPhone 5c"},
    {"identifier": "iPhone6,1", "description": "iPhone 5s"},
    {"identifier": "iPhone6,2", "description": "iPhone 5s"},
    {"identifier": "iPhone7,1", "description": "iPhone 6 Plus"},
    {"identifier": "iPhone7,2", "description": "iPhone 6"},
    {"identifier": "iPhone8,1", "description": "iPhone 6s"},
    {"identifier": "iPhone8,2", "description": "iPhone 6s Plus"},
    {"identifier": "iPhone8,4", "description": "iPhone SE (1st generation)"},
    {"identifier": "iPhone9,1", "description": "iPhone 7"},
    {"identifier": "iPhone9,2", "description": "iPhone 7 Plus"},
    {"identifier": "iPhone9,3", "description": "iPhone 7"},
    {"identifier": "iPhone9,4", "description": "iPhone 7 Plus"},
    {"identifier": "iPhone10,1", "description": "iPhone 8"},
    {"identifier": "iPhone10,2", "description": "iPhone 8 Plus"},
    {"identifier": "iPhone10,3", "description": "iPhone X"},
    {"identifier": "iPhone10,4", "description": "iPhone 8"},
    {"identifier": "iPhone10,5", "description": "iPhone 8 Plus"},
    {"identifier": "iPhone10,6", "description": "iPhone X"},
    {"identifier": "iPhone11,2", "description": "iPhone XS"},
    {"identifier": "iPhone11,4", "description": "iPhone XS Max"},
    {"identifier": "iPhone11,6", "description": "iPhone XS Max"},
    {"identifier": "iPhone11,8", "description": "iPhone XR"},
    {"identifier": "iPhone12,1", "description": "iPhone 11"},
    {"identifier": "iPhone12,3", "description": "iPhone 11 Pro"},
    {"identifier": "iPhone12,5", "description": "iPhone 11 Pro Max"},
    {"identifier": "iPhone12,8", "description": "iPhone SE (2nd generation)"},
    {"identifier": "iPhone13,1", "description": "iPhone 12 mini"},
    {"identifier": "iPhone13,2", "description": "iPhone 12"},
    {"identifier": "iPhone13,3", "description": "iPhone 12 Pro"},
    {"identifier": "iPhone13,4", "description": "iPhone 12 Pro Max"},
    {"identifier": "iPhone14,4", "description": "iPhone 13 Mini"},
    {"identifier": "iPhone14,5", "description": "iPhone 13"},
    {"identifier": "iPhone14,2", "description": "iPhone 13 Pro"},
    {"identifier": "iPhone14,3", "description": "iPhone 13 Pro Max"},
]

IPHONE_IOS_VERSIONS = [
    {"build": "1A543a", "version": "1.0"},
    {"build": "1C25", "version": "1.0.1"},
    {"build": "1C28", "version": "1.0.2"},
    {"build": "3A109a", "version": "1.1.1"},
    {"build": "3B48b", "version": "1.1.2"},
    {"build": "4A93", "version": "1.1.3"},
    {"build": "4A102", "version": "1.1.4"},
    {"build": "5A347", "version": "2.0"},
    {"build": "5B108", "version": "2.0.1"},
    {"build": "5C1", "version": "2.0.2"},
    {"build": "5F136", "version": "2.1"},
    {"build": "5G77", "version": "2.2"},
    {"build": "5H11", "version": "2.2.1"},
    {"build": "7A341", "version": "3.0"},
    {"build": "7A400", "version": "3.0.1"},
    {"build": "7C144", "version": "3.1"},
    {"build": "7D11", "version": "3.1.2"},
    {"build": "7E18", "version": "3.1.3"},
    {"build": "8A293", "version": "4.0"},
    {"build": "8A306", "version": "4.0.1"},
    {"build": "8B117", "version": "4.1"},
    {"build": "8C148", "version": "4.2"},
    {"build": "8C148a", "version": "4.2.1"},
    {"build": "8C148", "version": "4.2.1"},
    {"build": "8E600", "version": "4.2.10"},
    {"build": "8E401", "version": "4.2.8"},
    {"build": "8E501", "version": "4.2.9"},
    {"build": "8F190", "version": "4.3"},
    {"build": "8J2", "version": "4.3.3"},
    {"build": "8K2", "version": "4.3.4"},
    {"build": "8L1", "version": "4.3.5"},
    {"build": "9A334", "version": "5.0"},
    {"build": "9A405", "version": "5.0.1"},
    {"build": "9A406", "version": "5.0.1"},
    {"build": "9B176", "version": "5.1"},
    {"build": "9B179", "version": "5.1"},
    {"build": "9B206", "version": "5.1.1"},
    {"build": "9B208", "version": "5.1.1"},
    {"build": "10A403", "version": "6.0"},
    {"build": "10A405", "version": "6.0"},
    {"build": "10A523", "version": "6.0.1"},
    {"build": "10A525", "version": "6.0.1"},
    {"build": "10A551", "version": "6.0.2"},
    {"build": "10B141", "version": "6.1"},
    {"build": "10B144", "version": "6.1"},
    {"build": "10B142", "version": "6.1"},
    {"build": "10B143", "version": "6.1"},
    {"build": "10B145", "version": "6.1.1"},
    {"build": "10B146", "version": "6.1.2"},
    {"build": "10B329", "version": "6.1.3"},
    {"build": "10B350", "version": "6.1.4"},
    {"build": "10B500", "version": "6.1.6"},
    {"build": "11B511", "version": "7.0.3"},
    {"build": "11B554a", "version": "7.0.4"},
    {"build": "11B601", "version": "7.0.5"},
    {"build": "11B651", "version": "7.0.6"},
    {"build": "11D169", "version": "7.1"},
    {"build": "11D167", "version": "7.1"},
    {"build": "11D201", "version": "7.1.1"},
    {"build": "11D257", "version": "7.1.2"},
    {"build": "12A365", "version": "8.0"},
    {"build": "12A366", "version": "8.0"},
    {"build": "12A402", "version": "8.0.1"},
    {"build": "12A405", "version": "8.0.2"},
    {"build": "12B411", "version": "8.1"},
    {"build": "12B435", "version": "8.1.1"},
    {"build": "12B436", "version": "8.1.1"},
    {"build": "12B440", "version": "8.1.2"},
    {"build": "12B466", "version": "8.1.3"},
    {"build": "12D508", "version": "8.2"},
    {"build": "12F70", "version": "8.3"},
    {"build": "12H143", "version": "8.4"},
    {"build": "12H321", "version": "8.4.1"},
    {"build": "13A344", "version": "9.0"},
    {"build": "13A342", "version": "9.0"},
    {"build": "13A343", "version": "9.0"},
    {"build": "13A404", "version": "9.0.1"},
    {"build": "13A405", "version": "9.0.1"},
    {"build": "13A452", "version": "9.0.2"},
    {"build": "13B143", "version": "9.1"},
    {"build": "13C75", "version": "9.2"},
    {"build": "13D15", "version": "9.2.1"},
    {"build": "13D20", "version": "9.2.1"},
    {"build": "13E237", "version": "9.3"},
    {"build": "13E233", "version": "9.3"},
    {"build": "13E234", "version": "9.3"},
    {"build": "13E238", "version": "9.3.1"},
    {"build": "13F69", "version": "9.3.2"},
    {"build": "13G34", "version": "9.3.3"},
    {"build": "13G35", "version": "9.3.4"},
    {"build": "13G36", "version": "9.3.5"},
    {"build": "13G37", "version": "9.3.6"},
    {"build": "14A403", "version": "10.0.1"},
    {"build": "14A456", "version": "10.0.2"},
    {"build": "14A551", "version": "10.0.3"},
    {"build": "14B72", "version": "10.1"},
    {"build": "14B72c", "version": "10.1"},
    {"build": "14B150", "version": "10.1.1"},
    {"build": "14B100", "version": "10.1.1"},
    {"build": "14C92", "version": "10.2"},
    {"build": "14D27", "version": "10.2.1"},
    {"build": "14E277", "version": "10.3"},
    {"build": "14E304", "version": "10.3.1"},
    {"build": "14F89", "version": "10.3.2"},
    {"build": "14G60", "version": "10.3.3"},
    {"build": "14G61", "version": "10.3.4"},
    {"build": "15A372", "version": "11.0"},
    {"build": "15A402", "version": "11.0.1"},
    {"build": "15A421", "version": "11.0.2"},
    {"build": "15A432", "version": "11.0.3"},
    {"build": "15B93", "version": "11.1"},
    {"build": "15B150", "version": "11.1.1"},
    {"build": "15B202", "version": "11.1.2"},
    {"build": "15C114", "version": "11.2"},
    {"build": "15C153", "version": "11.2.1"},
    {"build": "15C202", "version": "11.2.2"},
    {"build": "15D60", "version": "11.2.5"},
    {"build": "15D100", "version": "11.2.6"},
    {"build": "15E216", "version": "11.3"},
    {"build": "15E302", "version": "11.3.1"},
    {"build": "15F79", "version": "11.4"},
    {"build": "15G77", "version": "11.4.1"},
    {"build": "16A366", "version": "12.0"},
    {"build": "16A404", "version": "12.0.1"},
    {"build": "16A405", "version": "12.0.1"},
    {"build": "16B92", "version": "12.1"},
    {"build": "16B94", "version": "12.1"},
    {"build": "16B93", "version": "12.1"},
    {"build": "16C50", "version": "12.1.1"},
    {"build": "16C104", "version": "12.1.2"},
    {"build": "16C101", "version": "12.1.2"},
    {"build": "16D39", "version": "12.1.3"},
    {"build": "16D40", "version": "12.1.3"},
    {"build": "16D57", "version": "12.1.4"},
    {"build": "16E227", "version": "12.2"},
    {"build": "16F156", "version": "12.3"},
    {"build": "16F203", "version": "12.3.1"},
    {"build": "16F250", "version": "12.3.2"},
    {"build": "16G77", "version": "12.4"},
    {"build": "16G102", "version": "12.4.1"},
    {"build": "16G114", "version": "12.4.2"},
    {"build": "16G130", "version": "12.4.3"},
    {"build": "16G161", "version": "12.4.5"},
    {"build": "16G183", "version": "12.4.6"},
    {"build": "16G192", "version": "12.4.7"},
    {"build": "16G201", "version": "12.4.8"},
    {"build": "16H5", "version": "12.4.9"},
    {"build": "16H20", "version": "12.5"},
    {"build": "16H22", "version": "12.5.1"},
    {"build": "17A577", "version": "13.0"},
    {"build": "17A844", "version": "13.1"},
    {"build": "17A854", "version": "13.1.1"},
    {"build": "17A860", "version": "13.1.2"},
    {"build": "17A861", "version": "13.1.2"},
    {"build": "17A878", "version": "13.1.3"},
    {"build": "17B84", "version": "13.2"},
    {"build": "17B102", "version": "13.2.2"},
    {"build": "17B111", "version": "13.2.3"},
    {"build": "17C54", "version": "13.3"},
    {"build": "17D50", "version": "13.3.1"},
    {"build": "17E255", "version": "13.4"},
    {"build": "17E262", "version": "13.4.1"},
    {"build": "17E8258", "version": "13.4.1"},
    {"build": "17F75", "version": "13.5"},
    {"build": "17F80", "version": "13.5.1"},
    {"build": "17G68", "version": "13.6"},
    {"build": "17G80", "version": "13.6.1"},
    {"build": "17H35", "version": "13.7"},
    {"build": "18A373", "version": "14.0"},
    {"build": "18A393", "version": "14.0.1"},
    {"build": "18A8395", "version": "14.1"},
    {"build": "18B92", "version": "14.2"},
    {"build": "18C66", "version": "14.3"},
    {"build": "18D52", "version": "14.4"},
    {"build": "18D61", "version": "14.4.1"},
    {"build": "18D70", "version": "14.4.2"},
    {"build": "18E199", "version": "14.5"},
    {"build": "18E212", "version": "14.5.1"},
    {"build": "18F72", "version": "14.6"},
    {"build": "18G69", "version": "14.7"},
    {"build": "18G82", "version": "14.7.1"},
    {"build": "18H17", "version": "14.8"},
    {"build": "18H107", "version": "14.8.1"},
    {"build": "19A341", "version": "15.0"},
    {"build": "19A346", "version": "15.0"},
    {"build": "19A348", "version": "15.0.1"},
    {"build": "19A404", "version": "15.0.2"},
    {"build": "19B74", "version": "15.1"},
    {"build": "19B81", "version": "15.1.1"},
    {"build": "19C56", "version": "15.2"},
    {"build": "19C63", "version": "15.2.1"},
    {"build": "19D50", "version": "15.3"},
    {"build": "19D52", "version": "15.3.1"},
    {"build": "19E241", "version": "15.4"},
    {"build": "19E258", "version": "15.4.1"},
    {"build": "19F77", "version": "15.5"},
    {"build": "19G71", "version": "15.6"},
    {"build": "19G82", "version": "15.6.1"},
    {"build": "19H12", "version": "15.7"},
    {"build": "20A362", "version": "16.0"},
]


def get_device_desc_from_id(identifier: str,
                            devices_list: list = IPHONE_MODELS) -> str:
    for model in devices_list:
        if identifier == model["identifier"]:
            return model["description"]

    return ""


def find_version_by_build(build: str) -> str:
    build = build.upper()
    for version in IPHONE_IOS_VERSIONS:
        if build == version["build"]:
            return version["version"]

    return ""


def latest_ios_version() -> str:
    return IPHONE_IOS_VERSIONS[-1]
