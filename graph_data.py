# Realistic Bangalore Road Network (Directed, with Traffic)

graph = {

    # ---------------- Central Core ----------------
    "Majestic": [
        ("Malleswaram", 3, "Green"),      # two-way
        ("Rajajinagar", 2, "Green"),      # two-way
        ("Shivajinagar", 4, "Red"),       # one-way (towards east)
        ("Jayanagar", 6, "Green"),        # south corridor
        ("Yeshwanthpur", 5, "Red")        # north-west corridor
    ],

    "Malleswaram": [
        ("Majestic", 3, "Green"),
        ("Yeshwanthpur", 3, "Green"),
        ("Hebbal", 7, "Red")
    ],

    "Rajajinagar": [
        ("Majestic", 2, "Green"),
        ("Yeshwanthpur", 4, "Green"),
        ("RT Nagar", 6, "Red"),
        ("MG Road", 5, "Green")
    ],

    "Shivajinagar": [
        ("MG Road", 3, "Red"),            # one-way
        ("Ulsoor", 4, "Green")
    ],

    # ---------------- North Bangalore ----------------
    "Yeshwanthpur": [
        ("Hebbal", 5, "Green"),
        ("Peenya", 6, "Red"),
        ("Rajajinagar", 4, "Green")       # ring-road link
    ],

    "Hebbal": [
        ("Manyata", 3, "Green"),
        ("KR Puram", 8, "Green"),
        ("RT Nagar", 4, "Green")
    ],

    "RT Nagar": [
        ("Hebbal", 4, "Green"),
        ("MG Road", 7, "Red")
    ],

    "Peenya": [
        ("Nagasandra", 3, "Green")
    ],

    "Nagasandra": [
        ("Tumkur Road", 4, "Red")
    ],

    "Tumkur Road": [],

    "Manyata": [
        ("Hebbal", 3, "Green")
    ],

    # ---------------- East Bangalore ----------------
    "MG Road": [
        ("Indiranagar", 4, "Green"),
        ("Ulsoor", 2, "Green"),
        ("Koramangala", 6, "Red")
    ],

    "Ulsoor": [
        ("Indiranagar", 3, "Green"),
        ("Banashankari", 7, "Red")
    ],

    "Indiranagar": [
        ("Whitefield", 8, "Green"),
        ("Marathahalli", 5, "Green"),
        ("KR Puram", 4, "Red")
    ],

    "KR Puram": [
        ("Marathahalli", 3, "Green"),
        ("BTM Layout", 6, "Red"),
        ("Hebbal", 8, "Green")            # ring-road
    ],

    "Whitefield": [
        ("ITPL", 2, "Green"),
        ("Sarjapur", 7, "Green")
    ],

    "ITPL": [],

    "Marathahalli": [
        ("Sarjapur", 5, "Green"),
        ("Electronic City", 10, "Red")
    ],

    "Sarjapur": [
        ("Electronic City", 5, "Green"),
        ("Whitefield", 7, "Green")        # two-way tech corridor
    ],

    # ---------------- South Bangalore ----------------
    "Koramangala": [
        ("BTM Layout", 2, "Green"),
        ("Jayanagar", 4, "Green")
    ],

    "BTM Layout": [
        ("Electronic City", 6, "Green"),
        ("Banashankari", 4, "Green")
    ],

    "Jayanagar": [
        ("Basavanagudi", 2, "Green"),
        ("Banashankari", 3, "Green"),
        ("Majestic", 6, "Green")          # north-south corridor
    ],

    "Basavanagudi": [
        ("Banashankari", 2, "Green")
    ],

    "Banashankari": [
        ("Electronic City", 9, "Red"),
        ("BTM Layout", 4, "Green")
    ],

    "Electronic City": [
        ("Sarjapur", 5, "Green"),
        ("Marathahalli", 10, "Red"),
        ("Banashankari", 9, "Red")        # ring-road south
    ]
}
