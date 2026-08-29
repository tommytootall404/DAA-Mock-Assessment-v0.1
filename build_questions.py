"""
Builds the DAA question bank.

    python3 build_questions.py

Writes questions.json and questions.js next to this script. index.html reads
questions.js, so re-run this after editing or adding questions, then refresh
the browser. To add questions by hand instead, edit questions.js directly:
each entry needs section, question, options (4), answer (0-3) and explanation.
"""
"""DAA question bank generator - part 1: verbal, numerical, work rate."""
import random, json

RNG = random.Random(2604)
BANK = []

def add(section, question, correct, wrongs, explanation, passage=None):
    """Build a multiple choice item. correct/wrongs are strings."""
    opts = [str(correct)]
    for w in wrongs:
        w = str(w)
        if w not in opts:
            opts.append(w)
        if len(opts) == 4:
            break
    if len(opts) < 4:
        return  # skip malformed item rather than pad with nonsense
    RNG.shuffle(opts)
    item = {
        "id": f"{section[:3]}{len(BANK):04d}",
        "section": section,
        "question": question,
        "options": opts,
        "answer": opts.index(str(correct)),
        "explanation": explanation,
    }
    if passage:
        item["passage"] = passage
    BANK.append(item)


# ---------------------------------------------------------------- VERBAL
VOCAB = [
    ("meticulous", "painstaking", ["careless", "hasty", "arrogant"], "showing very great attention to detail"),
    ("corrode", "eat away", ["strengthen", "polish", "insulate"], "gradual chemical wearing away of a material"),
    ("buoyant", "able to float", ["dense", "brittle", "rigid"], "able to stay afloat"),
    ("adjacent", "neighbouring", ["distant", "opposite", "concealed"], "next to or adjoining something"),
    ("concise", "brief", ["lengthy", "vague", "complicated"], "saying a lot in few words"),
    ("diligent", "hard-working", ["idle", "careless", "hesitant"], "showing steady, careful effort"),
    ("volatile", "unstable", ["solid", "dependable", "heavy"], "liable to change rapidly and unpredictably"),
    ("obsolete", "out of date", ["modern", "essential", "rapid"], "no longer in use because something newer exists"),
    ("rigorous", "thorough", ["relaxed", "casual", "hurried"], "extremely careful and exact"),
    ("mitigate", "reduce", ["worsen", "ignore", "postpone"], "to make something less severe"),
    ("prudent", "sensible", ["reckless", "generous", "hasty"], "acting with care and forethought"),
    ("tenacious", "persistent", ["weak", "flexible", "sudden"], "keeping a firm hold, not giving up"),
    ("ambiguous", "unclear", ["obvious", "honest", "brief"], "open to more than one interpretation"),
    ("resilient", "quick to recover", ["fragile", "stubborn", "sluggish"], "able to recover quickly from difficulty"),
    ("imminent", "about to happen", ["distant", "unlikely", "finished"], "due to occur very soon"),
    ("scrutinise", "examine closely", ["glance at", "disregard", "approve"], "to inspect in close detail"),
    ("redundant", "no longer needed", ["essential", "repeated", "faulty"], "surplus to requirements"),
    ("comply", "obey", ["refuse", "question", "delay"], "to act in accordance with an order or rule"),
    ("deteriorate", "get worse", ["improve", "stabilise", "expand"], "to decline in quality or condition"),
    ("abundant", "plentiful", ["scarce", "costly", "hidden"], "existing in large quantities"),
    ("hazardous", "dangerous", ["safe", "difficult", "expensive"], "carrying risk of harm"),
    ("alleviate", "ease", ["worsen", "prolong", "trigger"], "to make a problem less severe"),
    ("succinct", "to the point", ["rambling", "loud", "technical"], "expressed clearly in few words"),
    ("robust", "strong", ["delicate", "flexible", "lightweight"], "sturdy and able to withstand rough treatment"),
    ("impede", "hinder", ["assist", "accelerate", "permit"], "to get in the way of progress"),
    ("verify", "confirm", ["assume", "deny", "estimate"], "to check that something is true"),
    ("intermittent", "occurring in bursts", ["constant", "permanent", "increasing"], "stopping and starting irregularly"),
    ("negligible", "very small", ["substantial", "urgent", "average"], "so small it can be ignored"),
    ("feasible", "achievable", ["impossible", "expensive", "compulsory"], "able to be done"),
    ("obstruct", "block", ["clear", "repair", "shorten"], "to get in the way of or block"),
]
for word, right, wrong, why in VOCAB:
    add("verbal", f"Which word is closest in meaning to <b>{word}</b>?", right, wrong,
        f"{word.capitalize()} means {why}.")

ODD = [
    (["Frigate", "Destroyer", "Submarine", "Harbour"], "Harbour", "A harbour is a place; the others are vessels."),
    (["Copper", "Aluminium", "Rubber", "Steel"], "Rubber", "Rubber is an insulator; the others are metals."),
    (["Spanner", "Hammer", "Screwdriver", "Workshop"], "Workshop", "A workshop is a place; the others are hand tools."),
    (["Voltage", "Current", "Resistance", "Spanner"], "Spanner", "A spanner is a tool; the others are electrical quantities."),
    (["Metre", "Fathom", "Mile", "Litre"], "Litre", "A litre measures volume; the others measure distance."),
    (["Ampere", "Volt", "Ohm", "Celsius"], "Celsius", "Celsius measures temperature; the others are electrical units."),
    (["Diesel", "Petrol", "Kerosene", "Copper"], "Copper", "Copper is a metal; the others are fuels."),
    (["Lever", "Pulley", "Gear", "Circuit"], "Circuit", "A circuit is electrical; the others are mechanical devices."),
    (["Hydraulic", "Pneumatic", "Electrical", "Rectangular"], "Rectangular", "Rectangular describes a shape; the others describe power systems."),
    (["Bow", "Stern", "Port", "Anchor"], "Anchor", "An anchor is equipment; the others name parts or sides of a ship."),
    (["Welding", "Soldering", "Brazing", "Sanding"], "Sanding", "Sanding removes material; the others join metals."),
    (["Kilogram", "Tonne", "Gram", "Second"], "Second", "A second measures time; the others measure mass."),
]
for opts, right, why in ODD:
    add("verbal", "Which is the odd one out?", right, [o for o in opts if o != right], why)

ANALOGY = [
    ("Anchor is to ship as foundation is to", "building", ["bricklayer", "cement", "ground"],
     "An anchor holds a ship in place; a foundation holds a building in place."),
    ("Volt is to voltage as ohm is to", "resistance", ["current", "power", "charge"],
     "Each is the unit used to measure that quantity."),
    ("Captain is to ship as pilot is to", "aircraft", ["runway", "engine", "passenger"],
     "Each is the person in command of that craft."),
    ("Fuel is to engine as food is to", "body", ["kitchen", "plate", "farmer"],
     "Each is the energy source consumed by the thing that follows."),
    ("Thermometer is to temperature as ammeter is to", "current", ["voltage", "resistance", "power"],
     "Each instrument measures the quantity that follows it."),
    ("Rudder is to direction as throttle is to", "speed", ["fuel", "noise", "steering"],
     "Each control governs the quantity that follows it."),
    ("Hammer is to nail as spanner is to", "nut", ["wood", "hand", "toolbox"],
     "Each tool is used to work on the fastener that follows."),
    ("Water is to pipe as current is to", "wire", ["switch", "battery", "lamp"],
     "Each flows through the conductor that follows it."),
    ("Sailor is to navy as soldier is to", "army", ["rifle", "uniform", "barracks"],
     "Each is a member of the service that follows."),
    ("Fuse is to overload as valve is to", "pressure", ["water", "metal", "pump"],
     "Each is a safety device that responds to the condition that follows."),
    ("Chart is to navigator as blueprint is to", "engineer", ["office", "paper", "customer"],
     "Each is the technical drawing the named person works from."),
    ("Insulator is to electricity as dam is to", "water", ["concrete", "river", "valley"],
     "Each blocks the flow of the thing that follows."),
]
for stem, right, wrong, why in ANALOGY:
    add("verbal", f"{stem}:", right, wrong, why)

COMPLETION = [
    ("Although the sea state was severe, the crew ______ the repair without incident.",
     "completed", ["abandoned", "prevented", "postponed"],
     "'Although' signals contrast: the bad conditions did not stop them."),
    ("The fault was ______ by a loose connection rather than a failed component.",
     "caused", ["repaired", "avoided", "detected"],
     "'Rather than a failed component' shows the sentence is naming the cause."),
    ("Because the pump had just been serviced, the engineer was ______ it would run reliably.",
     "confident", ["doubtful", "unaware", "annoyed"],
     "'Because it had just been serviced' supports a positive expectation."),
    ("The instructions were so ______ that no two people read them the same way.",
     "ambiguous", ["detailed", "brief", "official"],
     "Different readings is the definition of ambiguity."),
    ("Despite the ______ of spare parts, the team kept the generator running.",
     "shortage", ["abundance", "delivery", "quality"],
     "'Despite' signals an obstacle overcome, so a lack of parts fits."),
    ("The briefing was ______: five minutes, no wasted words.",
     "succinct", ["rambling", "confusing", "hesitant"],
     "The colon explains the word: short and efficient."),
    ("Regular inspection helps to ______ the risk of corrosion going unnoticed.",
     "reduce", ["increase", "guarantee", "conceal"],
     "Inspection lowers the chance of a fault being missed."),
    ("Sea trials will ______ whether the modification has actually worked.",
     "determine", ["assume", "ignore", "prevent"],
     "Trials are carried out to find out, which is what 'determine' means."),
    ("The technician worked ______, checking every joint twice before signing off.",
     "methodically", ["hastily", "reluctantly", "randomly"],
     "Checking every joint twice describes a careful, systematic approach."),
    ("The alarm proved ______; there was no fault when the panel was opened.",
     "false", ["accurate", "urgent", "delayed"],
     "No fault was found, so the alarm was not genuine."),
]
for stem, right, wrong, why in COMPLETION:
    add("verbal", f"Complete the sentence:<br><i>{stem}</i>", right, wrong, why)

SYLLOGISM = [
    ("All Royal Navy engineering technicians complete a foundation course before joining their first ship. "
     "Leading Hand Bryce is an engineering technician who joined her first ship last month.",
     "Bryce completed a foundation course",
     ["Bryce was top of her foundation course", "Everyone on Bryce's ship is a technician", "Bryce's ship is a frigate"],
     "The rule covers all technicians, and Bryce is one. The other options add information the passage does not give."),
    ("No sailor may go ashore without a valid liberty card.",
     "A sailor without a valid liberty card may not go ashore",
     ["Every sailor holding a valid card may go ashore", "All sailors hold valid cards", "Sailors on watch hold valid cards"],
     "The card is stated as necessary, not sufficient. Reversing that is the trap."),
    ("Only qualified divers are permitted to enter the tank. Petty Officer Grant entered the tank yesterday.",
     "Grant is a qualified diver",
     ["Grant is the only qualified diver", "All qualified divers entered the tank", "The tank is dangerous"],
     "If only qualified divers may enter and Grant entered, Grant must be qualified."),
    ("Every watchkeeper carries a radio. Some watchkeepers also carry a torch.",
     "Some people carrying torches also carry radios",
     ["All watchkeepers carry torches", "Anyone with a radio is a watchkeeper", "Torches are issued to all crew"],
     "The watchkeepers with torches all carry radios too, so the overlap must exist."),
    ("All items in the forward store are flammable. Nothing flammable may be kept near the galley.",
     "No item from the forward store may be kept near the galley",
     ["The galley contains no flammable items", "The forward store is near the galley", "All flammable items are in the forward store"],
     "Chaining the two rules gives the conclusion directly."),
    ("Any generator that fails its monthly test is taken out of service. Generator 3 is in service today.",
     "Generator 3 did not fail its last monthly test",
     ["Generator 3 has never failed a test", "Generator 3 is the newest unit", "All generators passed the test"],
     "If failing means removal, then still being in service means it did not fail."),
    ("Some ratings on the course hold a driving licence. All ratings on the course passed the entrance test.",
     "Some licence holders on the course passed the entrance test",
     ["All ratings hold a driving licence", "Everyone who passed holds a licence", "The entrance test includes driving"],
     "Every rating on the course passed, including those with licences."),
    ("Whenever the alarm sounds, the compartment is evacuated. The compartment was not evacuated this morning.",
     "The alarm did not sound this morning",
     ["The alarm is broken", "The compartment was empty", "Evacuation drills are monthly"],
     "If the alarm always causes evacuation, no evacuation means no alarm."),
    ("All members of the ship's football team are under 30. Chief Petty Officer Doyle is 34.",
     "Doyle is not a member of the ship's football team",
     ["Doyle does not play football", "The team has no chief petty officers", "Doyle is the oldest on board"],
     "Doyle fails the stated condition for membership, so cannot be a member."),
    ("Every tool issued from the workshop must be signed for. A torque wrench is missing from the rack.",
     "If the wrench was issued, someone signed for it",
     ["The wrench was stolen", "The signing system has failed", "The wrench was never in the rack"],
     "Only the signing rule is stated; how the wrench went missing is not."),
    ("All engine room watches are stood in pairs. Able Rate Nolan is standing an engine room watch.",
     "At least one other person is standing that watch with Nolan",
     ["Nolan is the senior of the pair", "Nolan stands every watch in pairs", "There are only two watchkeepers on board"],
     "'In pairs' means a second person must be present."),
    ("No one may operate the crane without a current ticket. All tickets expire after two years.",
     "Someone whose ticket expired three years ago may not operate the crane",
     ["Everyone with a ticket operates the crane", "Tickets are renewed automatically", "The crane is rarely used"],
     "An expired ticket is not current, so the prohibition applies."),
]
for passage, right, wrong, why in SYLLOGISM:
    add("verbal", "Based only on the passage above, which conclusion <b>must</b> be true?", right, wrong, why, passage=passage)

TF_PASSAGE = [
    ("The ship's company works a watch system. Each watch is four hours long, except the two dog watches, "
     "which are two hours each. Watchkeepers must be relieved five minutes before the hour.",
     "A watchkeeper on the first dog watch is on watch for four hours.", "False",
     "The passage states dog watches are two hours each."),
    ("The ship's company works a watch system. Each watch is four hours long, except the two dog watches, "
     "which are two hours each. Watchkeepers must be relieved five minutes before the hour.",
     "Watchkeepers arrive at their post before the hour.", "True",
     "Relief five minutes before the hour is stated directly."),
    ("The ship's company works a watch system. Each watch is four hours long, except the two dog watches, "
     "which are two hours each. Watchkeepers must be relieved five minutes before the hour.",
     "The dog watches are the least popular watches to stand.", "Cannot tell",
     "The passage says nothing about how watches are regarded."),
    ("Stores are delivered to the ship every Tuesday and Friday. Perishable items must be used within four days "
     "of delivery. Frozen items may be held for up to three months.",
     "A perishable item delivered on Friday must be used by the following Tuesday.", "True",
     "Friday plus four days is Tuesday, which is within the stated limit."),
    ("Stores are delivered to the ship every Tuesday and Friday. Perishable items must be used within four days "
     "of delivery. Frozen items may be held for up to three months.",
     "Frozen items are delivered only on Tuesdays.", "Cannot tell",
     "The passage gives delivery days and storage limits but does not link them to item type."),
    ("All new joiners complete a fire-fighting course in their first month. Those posted to a submarine also "
     "complete an escape and rescue course. Courses are run at the shore establishment.",
     "A new joiner posted to a submarine completes at least two courses.", "True",
     "The fire-fighting course applies to all new joiners, and submariners add a second."),
    ("All new joiners complete a fire-fighting course in their first month. Those posted to a submarine also "
     "complete an escape and rescue course. Courses are run at the shore establishment.",
     "Everyone who completes the escape and rescue course is posted to a submarine.", "Cannot tell",
     "The passage says submariners take it, not that only they do."),
    ("The generator is serviced every 500 running hours. It has run for 1,240 hours since it was installed and "
     "has been serviced twice.", "The generator is due a service.", "True",
     "Two services cover 1,000 hours; at 1,240 hours a third is overdue."),
]
for passage, statement, right, why in TF_PASSAGE:
    add("verbal", f"<i>Statement:</i> {statement}<br>This statement is:", right,
        [o for o in ["True", "False", "Cannot tell"] if o != right] + ["Partly true"], why, passage=passage)


# ------------------------------------------------------------- NUMERICAL
# speed = distance / time
for speed, hours in [(30, 4.5), (18, 5), (24, 3.5), (12, 7.5), (22, 6), (15, 8), (28, 4), (16, 5.5)]:
    dist = speed * hours
    d = int(dist) if dist == int(dist) else dist
    h = int(hours) if hours == int(hours) else hours
    add("numerical", f"A ship covers {d} nautical miles in {h} hours. What is its average speed?",
        f"{speed} knots", [f"{speed+5} knots", f"{speed-4} knots", f"{round(speed*1.5)} knots"],
        f"Speed = distance ÷ time = {d} ÷ {h} = {speed} knots.")

# percentage of a capacity
for cap, pct in [(4800, 35), (3600, 40), (2500, 62), (9000, 15), (7200, 45), (1800, 30), (5400, 25), (6000, 55)]:
    remain = int(cap * (100 - pct) / 100)
    add("numerical", f"A tank holds {cap:,} litres and is {pct}% full. How many litres are needed to fill it?",
        f"{remain:,}", [f"{int(cap*pct/100):,}", f"{int(remain/2):,}", f"{cap:,}"],
        f"{100-pct}% of {cap:,} = {remain:,} litres.")

# ratio share
for total, ratio in [(96, (3, 4, 5)), (120, (2, 3, 5)), (144, (1, 3, 8)), (72, (2, 3, 4)),
                     (180, (4, 5, 9)), (210, (2, 4, 8)), (150, (1, 2, 2)), (98, (2, 5, 7))]:
    parts = sum(ratio)
    if total % parts:
        continue
    unit = total // parts
    big = unit * max(ratio)
    add("numerical", f"{total} items are shared between three stores in the ratio {':'.join(map(str,ratio))}. How many go to the largest share?",
        big, [unit * min(ratio), unit * sorted(ratio)[1], big + unit],
        f"{'+'.join(map(str,ratio))} = {parts} parts; {total} ÷ {parts} = {unit} per part; {max(ratio)} × {unit} = {big}.")

# percentage decrease / increase
for base, pct, up in [(250, 18, False), (400, 12, False), (320, 25, True), (180, 15, True),
                      (500, 8, False), (640, 45, False), (220, 30, True), (750, 6, False)]:
    res = base * (100 + pct if up else 100 - pct) / 100
    res = int(res) if res == int(res) else round(res, 1)
    other = base * (100 - pct if up else 100 + pct) / 100
    other = int(other) if other == int(other) else round(other, 1)
    verb = "increased" if up else "reduced"
    add("numerical", f"A ship's company of {base} is {verb} by {pct}%. How many are there now?",
        res, [other, int(base * pct / 100), base],
        f"{100+pct if up else 100-pct}% of {base} = {res}.")

# people-hours
for people, hours, newp in [(3, 8, 4), (5, 6, 3), (4, 9, 6), (2, 12, 8), (6, 10, 4), (9, 4, 3), (8, 3, 2), (10, 6, 5)]:
    total = people * hours
    if total % newp:
        continue
    add("numerical", f"{people} technicians take {hours} hours to finish a repair. Working at the same rate, how long would {newp} technicians take?",
        f"{total//newp} hours", [f"{hours} hours", f"{total//newp + 2} hours", f"{max(1,total//newp - 2)} hours"],
        f"{people} × {hours} = {total} technician-hours; {total} ÷ {newp} = {total//newp} hours.")

# sequences
SEQ = [
    ([3, 7, 15, 31], 63, "Each term doubles and adds 1."),
    ([96, 48, 24, 12], 6, "Each term is halved."),
    ([2, 6, 18, 54], 162, "Each term is multiplied by 3."),
    ([1, 4, 9, 16, 25], 36, "These are the square numbers."),
    ([5, 11, 23, 47], 95, "Each term doubles and adds 1."),
    ([100, 91, 83, 76], 70, "The gap shrinks by one each time: -9, -8, -7, -6."),
    ([2, 3, 5, 8, 13], 21, "Each term is the sum of the two before it."),
    ([7, 14, 28, 56], 112, "Each term doubles."),
    ([64, 32, 16, 8], 4, "Each term is halved."),
    ([1, 8, 27, 64], 125, "These are the cube numbers."),
    ([11, 22, 33, 44], 55, "The sequence rises in steps of 11."),
    ([3, 6, 12, 24, 48], 96, "Each term doubles."),
    ([90, 78, 66, 54], 42, "The sequence falls in steps of 12."),
    ([4, 9, 19, 39], 79, "Each term doubles and adds 1."),
]
for seq, nxt, why in SEQ:
    add("numerical", f"What comes next in the sequence?<br><b>{', '.join(map(str,seq))}, ?</b>",
        nxt, [nxt + seq[-1] - seq[-2] if len(seq) > 1 else nxt + 1, nxt - 2, nxt * 2],
        why)

# averages
AVG = [
    ([420, 380, 510, 290, 400], "litres of fuel used"),
    ([12, 18, 15, 21, 14], "faults logged"),
    ([64, 72, 58, 66], "stores items issued"),
    ([31, 27, 35, 29, 33], "engine hours run"),
    ([220, 260, 180, 240], "litres of water used"),
    ([8, 11, 14, 9, 13], "signals received"),
]
for vals, label in AVG:
    mean = sum(vals) / len(vals)
    m = int(mean) if mean == int(mean) else round(mean, 1)
    add("numerical", f"Daily figures for {label}: {', '.join(map(str,vals))}. What is the mean?",
        m, [max(vals), min(vals), round(m + 10, 1)],
        f"Total {sum(vals)} ÷ {len(vals)} days = {m}.")

# time durations
TIMES = [("2145", "0630", 8, 45), ("0730", "1415", 6, 45), ("2250", "0505", 6, 15),
         ("1840", "0210", 7, 30), ("0455", "1320", 8, 25), ("2315", "0800", 8, 45),
         ("1105", "1950", 8, 45), ("0320", "1145", 8, 25)]
for dep, arr, h, m in TIMES:
    corr = f"{h} hours {m} minutes"
    add("numerical", f"A ship departs at {dep} and arrives at {arr}. How long was the passage?",
        corr, [f"{h+1} hours {m} minutes", f"{h} hours {(m+30)%60} minutes", f"{h-1} hours {m} minutes"],
        f"Counting forward from {dep} to {arr} gives {h} hours {m} minutes.")

# area x unit cost
for w, l, rate in [(2.4, 1.5, 12.50), (3.0, 2.0, 8.40), (1.6, 2.5, 15.00), (4.0, 1.25, 9.60),
                   (2.2, 3.0, 11.00), (5.0, 1.4, 7.50)]:
    area = round(w * l, 2)
    cost = round(area * rate, 2)
    add("numerical", f"A steel plate measures {w} m by {l} m. At £{rate:.2f} per square metre, what does it cost?",
        f"£{cost:.2f}", [f"£{cost*2:.2f}", f"£{cost/2:.2f}", f"£{cost+rate:.2f}"],
        f"Area = {w} × {l} = {area} m²; {area} × £{rate:.2f} = £{cost:.2f}.")

# fuel per hour
for total, hours in [(1440, 12), (2100, 15), (960, 8), (3300, 22), (1800, 24), (2560, 16)]:
    rate = total // hours
    add("numerical", f"An engine burns {total:,} litres of fuel in {hours} hours. What is the hourly consumption?",
        f"{rate} litres", [f"{rate*2} litres", f"{rate//2} litres", f"{rate+10} litres"],
        f"{total:,} ÷ {hours} = {rate} litres per hour.")

# fractions of a quantity
for total, num, den in [(360, 3, 8), (480, 5, 6), (252, 4, 7), (200, 3, 5), (144, 5, 12), (330, 2, 11)]:
    val = total * num // den
    add("numerical", f"What is {num}/{den} of {total}?", val, [total * num // (den + 1), val + den, total // den],
        f"{total} ÷ {den} = {total//den}; {total//den} × {num} = {val}.")

# conversions and rates
add("numerical", "A pump moves 45 litres per minute. How many litres in three quarters of an hour?",
    "2,025", ["1,350", "2,700", "675"], "45 × 45 minutes = 2,025 litres.")
add("numerical", "A journey of 210 miles is driven at an average of 60 mph. How long does it take?",
    "3 hours 30 minutes", ["3 hours 15 minutes", "3 hours 50 minutes", "4 hours"],
    "210 ÷ 60 = 3.5 hours, which is 3 hours 30 minutes.")
add("numerical", "A crate weighs 18 kg. What is the total weight of 24 crates?",
    "432 kg", ["402 kg", "342 kg", "480 kg"], "18 × 24 = 432 kg.")
add("numerical", "A part costs £4.80. A store buys 35 of them. What is the total cost?",
    "£168.00", ["£148.00", "£172.80", "£158.40"], "4.80 × 35 = £168.00.")
add("numerical", "12 of a batch of 300 components fail inspection. What percentage failed?",
    "4%", ["12%", "3.6%", "40%"], "12 ÷ 300 = 0.04, which is 4%.")
add("numerical", "A generator runs for 7 hours 45 minutes on Monday and 5 hours 40 minutes on Tuesday. What is the total?",
    "13 hours 25 minutes", ["12 hours 85 minutes", "13 hours 5 minutes", "12 hours 25 minutes"],
    "45 + 40 = 85 minutes, which is 1 hour 25 minutes; 7 + 5 + 1 = 13 hours 25 minutes.")
add("numerical", "A tank loses 8 litres per hour through a leak. How much is lost in two and a half days?",
    "480 litres", ["400 litres", "192 litres", "960 litres"], "2.5 days = 60 hours; 60 × 8 = 480 litres.")
add("numerical", "Three quarters of a 68-person watch are on duty. How many is that?",
    "51", ["47", "54", "45"], "68 ÷ 4 = 17; 17 × 3 = 51.")
add("numerical", "A price of £250 is increased by 20%, then reduced by 20%. What is the final price?",
    "£240", ["£250", "£260", "£200"], "250 × 1.2 = 300; 300 × 0.8 = £240. Percentage changes do not cancel out.")
add("numerical", "A box of 144 bolts is shared equally between 9 workbenches. How many per bench?",
    "16", ["12", "18", "14"], "144 ÷ 9 = 16.")
add("numerical", "A shift starts at 0545 and lasts 9 hours 20 minutes. When does it end?",
    "1505", ["1445", "1525", "1405"], "0545 plus 9 hours is 1445; plus 20 minutes is 1505.")
add("numerical", "Two thirds of a 480-litre tank is used. How much remains?",
    "160 litres", ["320 litres", "240 litres", "120 litres"], "One third remains: 480 ÷ 3 = 160 litres.")

# ------------------------------------------------------------- WORK RATE
KEY = {"A": "\u25b3", "B": "\u25cb", "C": "\u25a1", "D": "\u00d7", "E": "\u25c7"}
INV = {v: k for k, v in KEY.items()}
KEYLINE = "Key: " + ", ".join(f"{k} = {v}" for k, v in KEY.items())
words = ["BEAD", "CAB", "DECADE", "FACE".replace("F", "B"), "ACE", "BADE", "CEDE", "DEAD",
         "ABC", "EDDA", "CAB", "BEE", "ADD", "BAD", "CAD", "DAB"]
seen = set()
for w in words:
    if w in seen:
        continue
    seen.add(w)
    enc = "".join(KEY[c] for c in w)
    wrong = ["".join(KEY[c] for c in w[::-1]),
             "".join(KEY[c] for c in (w[1:] + w[0])),
             "".join(KEY[c] for c in (w[:-1] + ("A" if w[-1] != "A" else "B")))]
    add("workrate", f"{KEYLINE}<br>Encode <b>{w}</b>:", enc, wrong,
        f"{' '.join(f'{c}={KEY[c]}' for c in w)}.")
for w in ["CAD", "BEAD", "DACE", "ACE", "EBB", "CEDE", "BADE", "DEAD"]:
    enc = "".join(KEY[c] for c in w)
    add("workrate", f"{KEYLINE}<br>Decode <b>{enc}</b>:", w, [w[::-1], w[1:] + w[0], w[:-1] + "E" if w[-1] != "E" else w[:-1] + "A"],
        f"Reading each symbol against the key gives {w}.")

# identical string matching
def scramble(s, rng):
    i = rng.randrange(len(s))
    pool = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    c = rng.choice([p for p in pool if p != s[i]])
    return s[:i] + c + s[i+1:]

for _ in range(10):
    core = "".join(RNG.choice("ABCDEFGHJKLMNPQRSTUVWXYZ") if i in (1, 4) else RNG.choice("23456789") for i in range(4))
    target = f"{core[:2]}-{core[2:]}{RNG.choice('KLMPRT')}{RNG.randrange(10)}"
    wrongs = []
    while len(wrongs) < 3:
        w = scramble(target.replace("-", ""), RNG)
        w = w[:2] + "-" + w[2:]
        if w != target and w not in wrongs:
            wrongs.append(w)
    add("workrate", f"Which option is identical to <b>{target}</b>?", target, wrongs,
        "The other three each change one character.")

# not-identical pair
for _ in range(8):
    pairs = []
    correct = None
    for i in range(4):
        n = "".join(str(RNG.randrange(10)) for _ in range(5))
        if i == 0:
            a, b = list(n), list(n)
            j = RNG.randrange(4)
            while b[j] == b[j+1]:
                n = "".join(str(RNG.randrange(10)) for _ in range(5))
                a, b = list(n), list(n)
                j = RNG.randrange(4)
            b[j], b[j+1] = b[j+1], b[j]
            correct = f"{n} / {''.join(b)}"
            pairs.append(correct)
        else:
            pairs.append(f"{n} / {n}")
    add("workrate", "Which pair is <b>not</b> identical?", correct, pairs[1:],
        "In that pair two adjacent digits are swapped; the other three pairs match exactly.")

# letter counting
PHRASES = [("Stainless steel vessels resist stress", "s"), ("Engine room ratings report readiness", "r"),
           ("Marine engineering assessment session", "e"), ("Portside pressure testing procedure", "p"),
           ("Communications console monitoring", "o"), ("Technical training standards", "t"),
           ("Naval aviation maintenance manual", "a"), ("Damage control locker inventory", "c"),
           ("Submarine escape and rescue", "e"), ("Weapon engineering workshop", "w")]
for phrase, letter in PHRASES:
    n = phrase.lower().count(letter)
    add("workrate", f"How many times does the letter <b>{letter}</b> appear in:<br><i>{phrase}</i>",
        n, [n + 1, n - 1, n + 2], f"Counting every {letter} gives {n}.")

# day arithmetic
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for _ in range(10):
    start = RNG.randrange(7)
    days = RNG.choice([16, 23, 30, 45, 52, 61, 74, 88, 100, 19, 37, 66])
    end = (start + days) % 7
    add("workrate", f"If today is {DAYS[start]}, what day will it be in {days} days?",
        DAYS[end], [DAYS[(end+1) % 7], DAYS[(end-1) % 7], DAYS[(end+3) % 7]],
        f"{days} ÷ 7 = {days//7} remainder {days%7}; {DAYS[start]} plus {days%7} days is {DAYS[end]}.")

# largest / smallest decimals
for _ in range(8):
    base = RNG.randrange(20, 90) / 100
    vals = sorted({round(base, 2), round(base + 0.008, 3), round(base - 0.02, 3), round(base + 0.03, 2)})
    if len(vals) < 4:
        continue
    biggest = max(vals)
    ask_max = RNG.random() < 0.5
    target = biggest if ask_max else min(vals)
    add("workrate", f"Which value is the {'largest' if ask_max else 'smallest'}?",
        f"{target:g}", [f"{v:g}" for v in vals if v != target],
        "Line the numbers up to the same number of decimal places and compare.")

# BODMAS speed arithmetic
for _ in range(12):
    a, b, c, d = RNG.randrange(3, 12), RNG.randrange(3, 12), RNG.randrange(2, 9), RNG.choice([2, 3, 4, 5])
    val = a * b - (c * d) // d if False else a * b - c
    expr = f"{a} × {b} − {c}"
    add("workrate", f"Work out: <b>{expr}</b>", val, [a * (b - c), val + c, a * b + c],
        f"Multiplication first: {a} × {b} = {a*b}; then {a*b} − {c} = {val}.")
for _ in range(8):
    a, b, c = RNG.randrange(4, 12), RNG.choice([12, 18, 24, 36, 48]), RNG.choice([2, 3, 4, 6])
    val = a + b // c
    add("workrate", f"Work out: <b>{a} + {b} ÷ {c}</b>", val, [(a + b) // c, a * b // c, val + 1],
        f"Division first: {b} ÷ {c} = {b//c}; then {a} + {b//c} = {val}.")

BANK_PART1 = BANK


# ---- part 2: spatial, mechanical, electrical ----

RNG = random.Random(7719)
BANK = []

def add(section, question, correct, wrongs, explanation, passage=None):
    opts = [str(correct)]
    for w in wrongs:
        w = str(w)
        if w not in opts:
            opts.append(w)
        if len(opts) == 4:
            break
    if len(opts) < 4:
        return
    RNG.shuffle(opts)
    item = {"id": f"{section[:3]}{len(BANK):04d}", "section": section, "question": question,
            "options": opts, "answer": opts.index(str(correct)), "explanation": explanation}
    if passage:
        item["passage"] = passage
    BANK.append(item)


# --------------------------------------------------------------- SPATIAL
# cube nets: middle row a,b,c,d ; e above b ; f below b
for _ in range(12):
    faces = RNG.sample(range(1, 10), 6)
    a, b, c, d, e, f = faces
    pairs = {a: c, c: a, b: d, d: b, e: f, f: e}
    ask = RNG.choice(faces)
    others = [x for x in faces if x not in (ask, pairs[ask])]
    add("spatial",
        f"A cube net is laid out flat. The middle row, left to right, reads <b>{a}, {b}, {c}, {d}</b>. "
        f"Face <b>{e}</b> sits directly above face {b}, and face <b>{f}</b> directly below face {b}. "
        f"When the net is folded, which face is opposite face <b>{ask}</b>?",
        pairs[ask], others,
        "In a row of four faces, the 1st and 3rd are opposite and the 2nd and 4th are opposite. "
        f"The faces above and below the row ({e} and {f}) are opposite each other. So {ask} pairs with {pairs[ask]}.")

# painted cube counts
for n in [3, 4, 5, 6]:
    add("spatial", f"A {n} cm cube is painted on every outer surface, then cut into 1 cm cubes. "
        "How many small cubes have <b>exactly two</b> painted faces?",
        12 * (n - 2), [8, 6 * (n - 2) ** 2, (n - 2) ** 3],
        f"Two painted faces means an edge cube that is not a corner. A cube has 12 edges, each with {n} − 2 = {n-2} such cubes: 12 × {n-2} = {12*(n-2)}.")
    add("spatial", f"A {n} cm cube is painted on every outer surface, then cut into 1 cm cubes. "
        "How many have <b>no</b> paint at all?",
        (n - 2) ** 3, [12 * (n - 2), 8, 6 * (n - 2) ** 2],
        f"The unpainted cubes form a hidden core of side {n} − 2 = {n-2}: {n-2}³ = {(n-2)**3}.")
    add("spatial", f"A {n} cm cube is painted on every outer surface, then cut into 1 cm cubes. "
        "How many have <b>exactly one</b> painted face?",
        6 * (n - 2) ** 2, [12 * (n - 2), 8, (n - 2) ** 3],
        f"One painted face means a cube in the middle of a face: 6 faces × ({n}−2)² = {6*(n-2)**2}.")
    add("spatial", f"A {n} cm cube is painted on every outer surface, then cut into 1 cm cubes. "
        "How many have <b>exactly three</b> painted faces?",
        8, [12 * (n - 2), 6 * (n - 2) ** 2, 12],
        "Three painted faces means a corner cube, and every cube has 8 corners whatever its size.")

# dice
for _ in range(8):
    top = RNG.randrange(1, 7)
    front = RNG.choice([x for x in range(1, 7) if x not in (top, 7 - top)])
    add("spatial", f"On a standard die, opposite faces total 7. The top face shows <b>{top}</b> and the front face shows <b>{front}</b>. "
        "What is on the bottom and the back?",
        f"Bottom {7-top}, back {7-front}", [f"Bottom {7-front}, back {7-top}", f"Bottom {top}, back {front}",
                                            f"Bottom {7-top}, back {front}"],
        f"7 − {top} = {7-top} on the bottom; 7 − {front} = {7-front} on the back.")

# rotation of a pointer
DIRS = ["up", "right", "down", "left"]
for _ in range(10):
    start = RNG.randrange(4)
    turns = RNG.choice([90, 180, 270])
    cw = RNG.random() < 0.5
    step = turns // 90
    end = (start + step) % 4 if cw else (start - step) % 4
    add("spatial", f"An arrow points <b>{DIRS[start]}</b>. It is rotated <b>{turns}° {'clockwise' if cw else 'anticlockwise'}</b>. Which way does it point now?",
        DIRS[end].capitalize(), [DIRS[(end+1) % 4].capitalize(), DIRS[(end+2) % 4].capitalize(), DIRS[(end+3) % 4].capitalize()],
        f"Each 90° {'clockwise' if cw else 'anticlockwise'} step moves the arrow one position round, ending {DIRS[end]}.")

# mirror words
MIRROR_OK = ["MUM", "TOOT", "WOW", "OTTO", "TOT", "AHA", "MAM", "YAY", "OXO", "HAH"]
NORMAL = ["DECK", "SHIP", "BOAT", "MAST", "HULL", "CREW", "DRILL", "ANCHOR", "WATCH", "RIG"]
for w in MIRROR_OK:
    add("spatial", "Which word, held up to a mirror, appears <b>unchanged</b>?", w, RNG.sample(NORMAL, 3),
        f"A mirror flips left to right. Every letter in {w} is symmetrical about a vertical axis, and the word reads the same backwards, so it survives the flip.")

# stacked cube counting
for base, removed in [(3, 4), (4, 6), (3, 9), (5, 20), (4, 12), (2, 3)]:
    total = base ** 3 - removed
    add("spatial", f"A solid cube {base} blocks wide, {base} deep and {base} high is built, then {removed} blocks are removed. How many blocks remain?",
        total, [base ** 3, total - base, total + removed],
        f"{base}³ = {base**3} blocks; {base**3} − {removed} = {total}.")

# solids
SOLIDS = [("cube", 6, 12, 8), ("triangular prism", 5, 9, 6), ("square-based pyramid", 5, 8, 5),
          ("cuboid", 6, 12, 8), ("tetrahedron", 4, 6, 4), ("hexagonal prism", 8, 18, 12)]
for name, f, e, v in SOLIDS:
    add("spatial", f"How many <b>faces</b> does a {name} have?", f, [f + 1, f - 1, f + 2],
        f"A {name} has {f} faces, {e} edges and {v} vertices.")
    add("spatial", f"How many <b>edges</b> does a {name} have?", e, [e + 2, e - 2, e + 4],
        f"A {name} has {e} edges.")

# 2D nets and views
add("spatial", "A rectangular sheet 90 cm by 40 cm is rotated 90° in its own plane. What are its dimensions now?",
    "40 cm by 90 cm", ["90 cm by 40 cm", "45 cm by 20 cm", "180 cm by 80 cm"],
    "Rotating a shape changes its orientation but never its size.")
add("spatial", "A cylinder is cut straight across, at right angles to its long axis. What shape is the cut face?",
    "A circle", ["A rectangle", "An oval", "A triangle"],
    "A cut at right angles to the axis of a cylinder always exposes a circle.")
add("spatial", "A cylinder is cut lengthways down its long axis. What shape is the cut face?",
    "A rectangle", ["A circle", "A triangle", "An oval"],
    "Cutting along the axis exposes a rectangle whose sides are the height and the diameter.")
add("spatial", "Viewed from directly above, what shape does a cone appear as?",
    "A circle", ["A triangle", "A square", "A semicircle"],
    "From above only the circular base outline is visible.")
add("spatial", "Viewed from the side, what shape does a cone appear as?",
    "A triangle", ["A circle", "A rectangle", "A diamond"],
    "From the side the sloping sides and the base form a triangle.")
add("spatial", "How many lines of symmetry does a rectangle that is not a square have?",
    "2", ["1", "4", "0"], "One vertical and one horizontal line only; the diagonals are not lines of symmetry.")
add("spatial", "How many lines of symmetry does an equilateral triangle have?",
    "3", ["1", "2", "6"], "One through each vertex to the midpoint of the opposite side.")
add("spatial", "A shape is reflected in a vertical mirror line and then reflected again in the same line. The result is:",
    "The original shape", ["A rotation of 90°", "An upside-down shape", "A larger shape"],
    "Two reflections in the same line cancel out.")
add("spatial", "Which of these is <b>not</b> a possible cross-section of a cube?",
    "A circle", ["A square", "A triangle", "A hexagon"],
    "A cube has only flat faces and straight edges, so every cross-section has straight sides.")
add("spatial", "A flag on a vertical pole points to the left. The pole is turned 180°. The flag now points:",
    "To the right", ["To the left", "Upwards", "Downwards"],
    "A half turn reverses left and right.")
add("spatial", "A gear wheel is rotated 360°. Compared with its starting position it is:",
    "Exactly as it started", ["Upside down", "Mirrored", "Turned a quarter"],
    "A full turn returns any object to its starting orientation.")
add("spatial", "Two identical right-angled triangles are joined along their longest sides. What shape can they form?",
    "A rectangle", ["A pentagon", "A circle", "A hexagon"],
    "Joining two congruent right-angled triangles along the hypotenuse forms a rectangle.")


# ------------------------------------------------------------ MECHANICAL
# gear ratio
for ta, tb, rpm in [(20, 60, 30), (15, 45, 60), (12, 36, 24), (25, 50, 40), (10, 40, 80), (18, 54, 27),
                    (30, 60, 22), (16, 48, 36)]:
    out = rpm * ta // tb
    add("mechanical", f"Gear A has {ta} teeth and meshes directly with Gear B, which has {tb} teeth. "
        f"If A turns clockwise at {rpm} rpm, Gear B turns:",
        f"Anticlockwise at {out} rpm", [f"Clockwise at {out} rpm", f"Anticlockwise at {rpm*tb//ta} rpm",
                                        f"Clockwise at {rpm} rpm"],
        f"Meshed gears turn opposite ways. Speed = {rpm} × {ta} ÷ {tb} = {out} rpm. More teeth means slower.")

for n in [3, 4, 5, 6, 7]:
    same = n % 2 == 1
    add("mechanical", f"{n} gears are meshed in a straight line. If the first turns clockwise, the last turns:",
        "Clockwise" if same else "Anticlockwise",
        ["Anticlockwise" if same else "Clockwise", "It does not turn", "It depends on the number of teeth"],
        f"Each mesh reverses direction. With {n} gears there are {n-1} reversals, so the last gear turns "
        f"{'the same way as' if same else 'the opposite way to'} the first.")

# levers
for load, la, ea in [(600, 20, 100), (450, 15, 90), (800, 25, 100), (360, 12, 72), (900, 30, 120), (540, 18, 108)]:
    ma = ea // la
    effort = load // ma
    add("mechanical", f"A lever has its fulcrum {la} cm from the load and {ea} cm from the effort. "
        f"What effort is needed to lift a {load} N load?",
        f"{effort} N", [f"{load} N", f"{effort*2} N", f"{load*ma} N"],
        f"Mechanical advantage = {ea} ÷ {la} = {ma}, so effort = {load} ÷ {ma} = {effort} N.")

# moments / seesaw
for w1, d1, d2 in [(40, 3, 2), (60, 2, 4), (30, 4, 3), (50, 3, 5), (80, 1.5, 2), (24, 5, 4)]:
    w2 = w1 * d1 / d2
    w2 = int(w2) if w2 == int(w2) else round(w2, 1)
    add("mechanical", f"A beam balances on a central pivot. A {w1} kg mass sits {d1} m from the pivot on one side. "
        f"What mass, placed {d2} m from the pivot on the other side, will balance it?",
        f"{w2} kg", [f"{w1} kg", f"{round(w1*d2/d1,1)} kg", f"{round(w2*2,1)} kg"],
        f"Balance needs equal moments: {w1} × {d1} = mass × {d2}, so mass = {w2} kg.")

# pulleys
for n, load in [(2, 120), (3, 150), (4, 200), (5, 250), (6, 300), (2, 90)]:
    add("mechanical", f"In a pulley system, {n} rope sections support the load. Ignoring friction, roughly what effort will lift a {load} kg load?",
        f"{load//n} kg", [f"{load} kg", f"{load//2 if n!=2 else load//4} kg", f"{load*n} kg"],
        f"The load is shared between {n} supporting sections: {load} ÷ {n} = {load//n} kg.")

# pressure
for force, area in [(500, 0.25), (900, 0.3), (240, 0.4), (1500, 0.5), (600, 0.15), (2000, 0.8)]:
    p = force / area
    p = int(p) if p == int(p) else round(p, 1)
    add("mechanical", f"A force of {force} N acts on an area of {area} m². What is the pressure?",
        f"{p:,} Pa", [f"{round(force*area,1)} Pa", f"{round(p/2,1)} Pa", f"{round(p*2,1)} Pa"],
        f"Pressure = force ÷ area = {force} ÷ {area} = {p:,} Pa.")

# hydraulics
for f1, a1, a2 in [(50, 2, 8), (30, 1, 6), (100, 4, 12), (25, 2, 10), (80, 5, 15)]:
    f2 = f1 * a2 // a1
    add("mechanical", f"A hydraulic press has a small piston of area {a1} cm² and a large piston of area {a2} cm². "
        f"A force of {f1} N on the small piston produces what force on the large one?",
        f"{f2} N", [f"{f1} N", f"{f1*a1//a2} N", f"{f2*2} N"],
        f"Pressure is equal throughout, so force scales with area: {f1} × ({a2} ÷ {a1}) = {f2} N.")

# springs
for x, n in [(8, 2), (12, 3), (20, 4), (9, 3), (16, 2)]:
    add("mechanical", f"A weight hung from one spring stretches it {x} cm. The same weight is hung from {n} identical springs side by side. Each spring now stretches:",
        f"{x//n} cm", [f"{x} cm", f"{x*n} cm", f"{x//n + 2} cm"],
        f"The weight is shared between {n} springs, so each carries 1/{n} of the load and stretches {x} ÷ {n} = {x//n} cm.")

# belt drives and conceptual mechanical
MECH_FIXED = [
    ("A single <b>fixed</b> pulley is used to raise a load. It:", "Changes the direction of the effort only",
     ["Halves the effort needed", "Quarters the effort needed", "Doubles the load that can be lifted"],
     "A fixed pulley gives no mechanical advantage; it just lets you pull down instead of up."),
    ("A single <b>moving</b> pulley is used to raise a load. Ignoring friction, it:", "Halves the effort needed",
     ["Doubles the effort needed", "Changes direction only", "Has no effect on effort"],
     "Two rope sections support a moving pulley, so the effort is halved (you pull twice the distance)."),
    ("Two pulleys are joined by a <b>crossed</b> belt. Compared with the driving pulley, the driven pulley turns:",
     "In the opposite direction", ["In the same direction", "At the same speed regardless of size", "Only if the pulleys match in size"],
     "Crossing the belt reverses the direction of the driven pulley."),
    ("Two pulleys are joined by an <b>open</b> (uncrossed) belt. The driven pulley turns:",
     "In the same direction", ["In the opposite direction", "At double the speed", "At half the speed"],
     "An open belt keeps both pulleys turning the same way."),
    ("A small pulley drives a much larger pulley by belt. The larger pulley turns:",
     "More slowly than the small one", ["Faster than the small one", "At the same speed", "In the opposite direction only"],
     "A larger pulley covers more circumference per turn, so it rotates more slowly."),
    ("Two people carry a plank with a heavy toolbox resting nearer one end. Who bears more weight?",
     "The person nearer the toolbox", ["The person further from the toolbox", "They bear equal weight", "It depends on the plank's length"],
     "The nearer support carries the larger share of the load."),
    ("Four sealed tanks of different shapes hold water to different depths. The pressure at the base depends mainly on:",
     "The depth of the water", ["The width of the tank", "The total volume held", "The material of the tank"],
     "Pressure at depth depends on the height of the water column, not the shape or volume."),
    ("A ship's rudder is put hard over to starboard. The stern of the ship initially swings:",
     "To port", ["To starboard", "It does not move sideways", "Downwards"],
     "The rudder pushes the stern to port, which is what swings the bow round to starboard."),
    ("Which arrangement gives the greatest mechanical advantage?",
     "Effort arm 50 cm, load arm 10 cm", ["Effort arm 10 cm, load arm 50 cm", "Effort arm 25 cm, load arm 25 cm", "Effort arm 40 cm, load arm 20 cm"],
     "Mechanical advantage = effort arm ÷ load arm. 50 ÷ 10 = 5, the highest of the four."),
    ("A steel block floats when placed in mercury but sinks in water. This is because:",
     "Mercury is denser than steel, water is not", ["Steel dissolves in water", "Mercury is a metal", "Water is colder"],
     "An object floats in any fluid denser than itself."),
    ("A screw thread is best described as which simple machine wrapped round a cylinder?",
     "An inclined plane", ["A lever", "A pulley", "A wheel and axle"],
     "A screw is an inclined plane wound helically, which is why it converts turning into large linear force."),
    ("Increasing the number of teeth on a driven gear will:",
     "Reduce its speed and increase its torque", ["Increase its speed and its torque", "Reduce both speed and torque", "Have no effect"],
     "Gearing down trades rotational speed for turning force."),
    ("A flywheel is fitted to an engine mainly to:",
     "Smooth out variations in speed", ["Increase fuel economy", "Cool the engine", "Reduce the weight"],
     "Its inertia stores energy between power strokes, evening out the rotation."),
    ("Two identical springs are joined <b>end to end</b> and the same weight is hung from them. Compared with one spring, the total stretch is:",
     "Twice as much", ["Half as much", "The same", "Four times as much"],
     "In series each spring carries the full load, so the extensions add."),
    ("A bearing is fitted between a rotating shaft and its housing mainly to:",
     "Reduce friction", ["Increase torque", "Add weight", "Insulate electrically"],
     "Bearings exist to reduce friction and wear between moving parts."),
    ("Water is pumped through a pipe that narrows. In the narrow section the water:",
     "Flows faster", ["Flows more slowly", "Stops", "Becomes denser"],
     "The same volume per second must pass through a smaller area, so velocity rises."),
    ("A load is dragged up a ramp rather than lifted straight up. The ramp:",
     "Reduces the force needed but increases the distance", ["Reduces both force and distance", "Increases the force needed", "Has no effect on the work done"],
     "A ramp is an inclined plane: less force over a longer distance, same work."),
    ("Which will float highest in water?",
     "A sealed empty drum", ["A drum half full of water", "A drum full of water", "A solid steel drum"],
     "The lower the average density, the higher the object floats."),
    ("A lever with the fulcrum <b>between</b> the effort and the load is which class?",
     "First class", ["Second class", "Third class", "Fourth class"],
     "First class levers (see-saw, crowbar, scissors) have the fulcrum in the middle."),
    ("A wheelbarrow, with the load between the wheel and the handles, is which class of lever?",
     "Second class", ["First class", "Third class", "Fourth class"],
     "Second class levers have the load between the fulcrum and the effort."),
    ("Turning a spanner with a longer handle makes the nut easier to undo because it:",
     "Increases the moment about the nut", ["Reduces the friction", "Increases the force applied by hand", "Reduces the load"],
     "Moment = force × distance, so a longer arm multiplies the turning effect."),
    ("A hydraulic system relies on the fact that liquids are:",
     "Virtually incompressible", ["Lighter than air", "Good conductors", "Highly compressible"],
     "Because the fluid does not compress, pressure applied at one piston is transmitted to the other."),
    ("A ship rolls less when its centre of gravity is:",
     "Lower", ["Higher", "Further forward", "Further aft"],
     "A lower centre of gravity increases stability and reduces rolling."),
    ("A four-stroke engine completes its cycle in how many strokes of the piston?",
     "Four", ["Two", "Three", "Six"],
     "Induction, compression, power and exhaust: four strokes, two crankshaft revolutions."),
]
for q, right, wrong, why in MECH_FIXED:
    add("mechanical", q, right, wrong, why)


# ------------------------------------------------------------ ELECTRICAL
# Ohm's law
for v, r in [(12, 4), (24, 6), (9, 3), (240, 60), (48, 8), (36, 12), (18, 9), (110, 22)]:
    add("electrical", f"A supply of {v} V is connected across a resistance of {r} Ω. What current flows?",
        f"{v//r} A", [f"{v*r} A", f"{round(r/v,2)} A", f"{v//r + 2} A"],
        f"I = V ÷ R = {v} ÷ {r} = {v//r} A.")
for i, r in [(3, 4), (2, 15), (5, 6), (0.5, 40), (4, 12), (6, 5)]:
    v = i * r
    v = int(v) if v == int(v) else v
    add("electrical", f"A current of {i} A flows through a resistance of {r} Ω. What is the voltage across it?",
        f"{v} V", [f"{round(r/i,1)} V", f"{v*2} V", f"{round(v/2,1)} V"],
        f"V = I × R = {i} × {r} = {v} V.")
for v, i in [(12, 2), (240, 10), (36, 3), (24, 8), (60, 5), (9, 6)]:
    r = v / i
    r = int(r) if r == int(r) else round(r, 1)
    add("electrical", f"A {v} V supply drives {i} A through a component. What is its resistance?",
        f"{r} Ω", [f"{v*i} Ω", f"{round(i/v,2)} Ω", f"{round(float(r)*2,1)} Ω"],
        f"R = V ÷ I = {v} ÷ {i} = {r} Ω.")

# power
for v, i in [(240, 5), (12, 10), (110, 4), (24, 15), (415, 2), (48, 6)]:
    add("electrical", f"A circuit operates at {v} V and draws {i} A. What is the power?",
        f"{v*i:,} W", [f"{v+i} W", f"{round(v/i,1)} W", f"{v*i*2:,} W"],
        f"P = V × I = {v} × {i} = {v*i:,} W.")
for i, r in [(3, 10), (2, 25), (5, 4), (4, 6), (6, 2)]:
    add("electrical", f"A current of {i} A flows through a {r} Ω resistor. What power is dissipated?",
        f"{i*i*r} W", [f"{i*r} W", f"{i*r*r} W", f"{i*i*r//2} W"],
        f"P = I² × R = {i}² × {r} = {i*i*r} W.")

# series / parallel
for a, b, v in [(3, 6, 18), (4, 8, 24), (5, 10, 30), (2, 4, 12), (7, 5, 36), (9, 3, 48)]:
    tot = a + b
    add("electrical", f"Resistors of {a} Ω and {b} Ω are connected <b>in series</b> across {v} V. What is the total resistance?",
        f"{tot} Ω", [f"{round(a*b/(a+b),2)} Ω", f"{abs(a-b)} Ω", f"{a*b} Ω"],
        f"Series resistances add: {a} + {b} = {tot} Ω.")
PAR = [(6, 3, 2), (12, 6, 4), (4, 4, 2), (20, 5, 4), (30, 60, 20), (9, 18, 6), (10, 15, 6), (8, 8, 4)]
for a, b, res in PAR:
    add("electrical", f"What is the total resistance of {a} Ω and {b} Ω connected <b>in parallel</b>?",
        f"{res} Ω", [f"{a+b} Ω", f"{abs(a-b)} Ω", f"{res*2} Ω"],
        f"({a} × {b}) ÷ ({a} + {b}) = {a*b} ÷ {a+b} = {res} Ω. Parallel resistance is always lower than the smallest branch.")

# cells
for n, cell in [(2, 1.5), (3, 1.5), (4, 1.5), (6, 2), (3, 2), (5, 1.5)]:
    tot = round(n * cell, 1)
    tot = int(tot) if tot == int(tot) else tot
    add("electrical", f"{n} cells of {cell} V each are connected <b>in series</b>. What is the total voltage?",
        f"{tot} V", [f"{cell} V", f"{round(cell/n,2)} V", f"{round(float(tot)*2,1)} V"],
        f"Series cells add their voltages: {n} × {cell} = {tot} V.")
    add("electrical", f"{n} cells of {cell} V each are connected <b>in parallel</b>. What is the total voltage?",
        f"{cell} V", [f"{tot} V", f"{round(cell*2,1)} V", f"{round(cell/n,2)} V"],
        f"Parallel cells keep the same voltage ({cell} V) but supply current for longer.")

# energy cost
for kw, hrs, rate in [(2, 5, 24), (3, 4, 30), (1.5, 8, 26), (0.5, 12, 28), (4, 3, 22)]:
    cost = kw * hrs * rate
    add("electrical", f"An appliance rated {kw} kW runs for {hrs} hours. At {rate}p per kWh, what does it cost?",
        f"£{cost/100:.2f}", [f"£{cost/50:.2f}", f"£{cost/200:.2f}", f"£{(kw*rate)/100:.2f}"],
        f"Energy = {kw} × {hrs} = {kw*hrs} kWh; {kw*hrs} × {rate}p = {cost:.0f}p = £{cost/100:.2f}.")

ELEC_FIXED = [
    ("Four identical bulbs are wired <b>in series</b>. One bulb fails open-circuit. What happens?",
     "All the bulbs go out", ["Only the failed bulb goes out", "The remaining bulbs get brighter", "Nothing changes"],
     "A series circuit has a single path, so breaking it anywhere stops all current."),
    ("Four identical bulbs are wired <b>in parallel</b>. One bulb fails open-circuit. What happens?",
     "Only the failed bulb goes out", ["All the bulbs go out", "The remaining bulbs get dimmer", "The supply voltage halves"],
     "Parallel branches are independent, so the others keep their full supply voltage."),
    ("Which is the best electrical conductor?", "Copper", ["Rubber", "Glass", "PVC"],
     "Copper is a metal with free electrons; the others are insulators."),
    ("Which of these is the best <b>insulator</b>?", "Rubber", ["Copper", "Aluminium", "Steel"],
     "Rubber resists the flow of current; the others are metals and conduct."),
    ("What is the purpose of a fuse?", "To break the circuit if the current gets too high",
     ["To increase the current", "To store charge", "To convert AC to DC"],
     "A fuse is a deliberate weak link that melts and disconnects the circuit under excess current."),
    ("In a circuit with a fixed supply voltage, if the resistance increases the current will:",
     "Decrease", ["Increase", "Stay the same", "Reverse direction"],
     "From I = V ÷ R, raising R with V fixed lowers I."),
    ("What is the unit of frequency?", "Hertz", ["Ohm", "Watt", "Coulomb"],
     "One hertz is one cycle per second. Ohm is resistance, watt is power, coulomb is charge."),
    ("What is the unit of electrical power?", "Watt", ["Volt", "Ampere", "Ohm"],
     "Power is measured in watts; volts measure potential difference and amperes measure current."),
    ("What is the unit of electrical resistance?", "Ohm", ["Volt", "Watt", "Hertz"],
     "Resistance is measured in ohms, symbol Ω."),
    ("In a simple circuit the switch is opened. What happens?", "Current stops flowing",
     ["Current keeps flowing", "Supply voltage falls to zero", "Resistance falls to zero"],
     "Opening a switch breaks the circuit, so no current can flow."),
    ("An ammeter should be connected:", "In series with the component",
     ["In parallel with the component", "Across the supply", "Either way round"],
     "All the current must pass through an ammeter, so it goes in series. A voltmeter goes in parallel."),
    ("A voltmeter should be connected:", "In parallel with the component",
     ["In series with the component", "In place of the fuse", "Between the two supply terminals only"],
     "A voltmeter measures the potential difference across a component, so it sits in parallel."),
    ("Earthing the metal case of an appliance is done to:", "Provide a safe path for fault current",
     ["Increase the supply voltage", "Reduce the running cost", "Improve the signal"],
     "An earth conductor carries fault current safely away and lets the protective device operate."),
    ("A circuit breaker differs from a fuse mainly because it:", "Can be reset rather than replaced",
     ["Works only on DC", "Increases the current rating", "Needs no wiring"],
     "Both interrupt excess current, but a breaker can be switched back on."),
    ("Doubling the voltage across a fixed resistance will:", "Double the current",
     ["Halve the current", "Leave the current unchanged", "Quadruple the resistance"],
     "I = V ÷ R, so with R fixed the current is proportional to voltage."),
    ("Three identical resistors are connected in parallel. The total resistance is:",
     "One third of one resistor", ["Three times one resistor", "The same as one resistor", "Twice one resistor"],
     "Identical resistors in parallel divide the resistance by the number of branches."),
    ("A transformer is used to:", "Change AC voltage from one level to another",
     ["Convert AC to DC", "Store electrical charge", "Measure current"],
     "Transformers step voltage up or down, and only work on alternating current."),
    ("A diode allows current to flow:", "In one direction only", ["In both directions", "Only at high voltage", "Only in AC circuits"],
     "A diode conducts in the forward direction and blocks the reverse."),
    ("A capacitor is a component that:", "Stores electrical charge", ["Converts AC to DC", "Increases resistance", "Measures voltage"],
     "A capacitor stores charge in an electric field between two plates."),
    ("A short circuit typically causes:", "A very large current to flow", ["No current to flow", "The voltage to rise", "The resistance to rise"],
     "A short offers a very low resistance path, so current rises sharply until protection operates."),
    ("The abbreviation AC stands for:", "Alternating current", ["Active current", "Applied charge", "Ampere count"],
     "AC reverses direction periodically; DC flows one way only."),
    ("Which material would you choose for the insulation on a cable?",
     "PVC", ["Copper", "Aluminium", "Brass"],
     "PVC is a non-conductor, which is what insulation requires."),
    ("Increasing the length of a wire, with everything else unchanged, will:",
     "Increase its resistance", ["Decrease its resistance", "Leave resistance unchanged", "Increase the voltage"],
     "Resistance is proportional to length and inversely proportional to cross-sectional area."),
    ("Increasing the thickness of a wire, with everything else unchanged, will:",
     "Decrease its resistance", ["Increase its resistance", "Leave resistance unchanged", "Reduce the current"],
     "A larger cross-sectional area gives current more room to flow, lowering resistance."),
    ("In a domestic UK plug, the live wire is coloured:", "Brown", ["Blue", "Green and yellow", "Black"],
     "Brown is live, blue is neutral, green and yellow is earth."),
    ("A battery is best described as a source of:", "Direct current", ["Alternating current", "Resistance", "Frequency"],
     "A battery supplies a steady one-directional (DC) current."),
]
for q, right, wrong, why in ELEC_FIXED:
    add("electrical", q, right, wrong, why)

BANK_PART2 = BANK


# ---- merge, de-duplicate, validate ----
import json, re
from collections import Counter, defaultdict

bank = BANK_PART1 + BANK_PART2

problems = []
seen = set()
clean = []
for q in bank:
    key = (q["question"], tuple(q["options"]), q.get("passage", ""))
    if key in seen:
        continue
    seen.add(key)
    if len(q["options"]) != 4:
        problems.append(("option count", q["question"][:60])); continue
    if len(set(q["options"])) != 4:
        problems.append(("duplicate options", q["question"][:60])); continue
    if not (0 <= q["answer"] < 4):
        problems.append(("bad answer index", q["question"][:60])); continue
    if not q["explanation"].strip():
        problems.append(("no explanation", q["question"][:60])); continue
    for o in q["options"]:
        if re.match(r"^-", o.strip()) or o.strip() in ("0", "0 A", "0 kg", "-1"):
            problems.append(("implausible option", q["question"][:60], o))
    clean.append(q)

order = ["verbal", "numerical", "workrate", "spatial", "mechanical", "electrical"]
by_sec = defaultdict(list)
for q in clean:
    by_sec[q["section"]].append(q)

final = []
for sec in order:
    for i, q in enumerate(by_sec[sec], 1):
        q["id"] = f"{sec[:4]}-{i:03d}"
        final.append(q)

print("problems:", problems[:20], "count", len(problems))
print(Counter(q["section"] for q in final))
print("TOTAL", len(final))
json.dump(final, open("questions.json", "w"), ensure_ascii=False, indent=1)

# --- second pass: replace any negative numeric distractor with a plausible positive one
import json as _j
data = _j.load(open("questions.json"))
fixed = 0
for q in data:
    correct = q["options"][q["answer"]]
    for i, o in enumerate(q["options"]):
        if i == q["answer"]:
            continue
        s = o.strip()
        if re.fullmatch(r"-\d+(\.\d+)?", s):
            n = abs(float(s))
            cand = int(n) + 1
            while str(cand) in q["options"]:
                cand += 3
            q["options"][i] = str(cand)
            fixed += 1
    assert len(set(q["options"])) == 4, q
    assert q["options"][q["answer"]] == correct
print("negative distractors replaced:", fixed)
_j.dump(data, open("questions.json", "w"), ensure_ascii=False, indent=1)

# ---- write the browser data file ----
qs = json.load(open("questions.json"))
with open("questions.js", "w", encoding="utf-8") as f:
    f.write("/* DAA question bank - generated by build_questions.py */\n")
    f.write("window.DAA_QUESTIONS = ")
    json.dump(qs, f, ensure_ascii=False, indent=1)
    f.write(";\n")
print("wrote questions.json and questions.js -", len(qs), "questions")
