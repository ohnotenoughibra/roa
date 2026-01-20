import json
import random
from datetime import datetime

# 13 NoGi topics
TOPICS = [
    "Guard Passing",
    "Guard Retention",
    "Half Guard",
    "Top Control",
    "Mount",
    "Back Control",
    "Front Headlock",
    "Turtle",
    "Escapes",
    "Submissions",
    "Leg Locks",
    "Takedowns",
    "Transitions"
]

# Constraint-led game templates for each topic
GAME_TEMPLATES = {
    "Guard Passing": [
        {
            "name": "Knee Slice Progression Game",
            "topPlayer": "Start in combat base, must touch inside thigh 3 times before attempting knee slice pass",
            "bottomPlayer": "Retain guard using frames and distance management",
            "coaching": "Top: Pressure through frames. Bottom: Active hips and grips",
            "skills": "#guardpassing #kneeSlice #pressure"
        },
        {
            "name": "Toreando Touch Game",
            "topPlayer": "Must touch both knees alternating 5 times before toreando pass",
            "bottomPlayer": "Keep feet between you and passer",
            "coaching": "Control the distance and angles",
            "skills": "#toreando #footwork #angles"
        },
        {
            "name": "Over-Under Pass Timer",
            "topPlayer": "Establish over-under grip, pass within 30 seconds or reset",
            "bottomPlayer": "Prevent hip control and create angles",
            "coaching": "Hip pressure vs hip escape",
            "skills": "#overunder #timing #pressure"
        },
        {
            "name": "Leg Drag Checkpoint",
            "topPlayer": "Must secure leg drag grip, touch hip, then complete pass",
            "bottomPlayer": "Recover guard before hip control established",
            "coaching": "Battle for inside control",
            "skills": "#legdrag #grips #control"
        },
        {
            "name": "Stack Pass Resistance",
            "topPlayer": "Stack opponent's hips and pass, bottom gets 2 points if they prevent stack",
            "bottomPlayer": "Post on mat and granby to prevent stack",
            "coaching": "Maintain posture and pressure",
            "skills": "#stackpass #posture #resistance"
        },
        {
            "name": "X-Pass Flow Game",
            "topPlayer": "Switch between toreando and knee slice every 10 seconds",
            "bottomPlayer": "Adapt guard retention to passing style",
            "coaching": "Read and react to pressure changes",
            "skills": "#adaptation #flow #reading"
        },
        {
            "name": "Long Step Pass Rush",
            "topPlayer": "Long step around guard, must keep both feet on mat",
            "bottomPlayer": "Hip escape to recover guard or get to knees",
            "coaching": "Speed vs timing",
            "skills": "#longstep #speed #recovery"
        },
        {
            "name": "Pressure Pass Battle",
            "topPlayer": "Heavy pressure through guard, can only advance by maintaining chest pressure",
            "bottomPlayer": "Create frames and angles to escape pressure",
            "coaching": "Constant pressure vs structural frames",
            "skills": "#pressure #frames #structure"
        },
        {
            "name": "Float Pass Sequence",
            "topPlayer": "Float pass attempt, if blocked switch to back step",
            "bottomPlayer": "Control distance and block hip movement",
            "coaching": "Chaining passing attempts",
            "skills": "#floatpass #chains #flow"
        },
        {
            "name": "Smash Pass Points",
            "topPlayer": "Smash pass from half guard, 2 points for mount finish",
            "bottomPlayer": "Prevent crossface and recover full guard",
            "coaching": "Control the head and shoulder line",
            "skills": "#smashpass #crossface #mount"
        },
        {
            "name": "Headquarters Position Game",
            "topPlayer": "Establish headquarters, score by maintaining position 10 seconds",
            "bottomPlayer": "Recover full guard or get to knees",
            "coaching": "Knee pressure control point",
            "skills": "#headquarters #control #position"
        },
        {
            "name": "Ankle Pick Pass",
            "topPlayer": "Pick ankle while passing, opponent can't use that leg for 5 seconds",
            "bottomPlayer": "Hop to maintain guard or recover",
            "coaching": "Off-balancing through leg attacks",
            "skills": "#anklepick #offbalance #timing"
        },
        {
            "name": "Backstep Challenge",
            "topPlayer": "Must backstep over leg, score by taking back or passing",
            "bottomPlayer": "Follow passer and recover guard",
            "coaching": "Movement creates opportunities",
            "skills": "#backstep #movement #back"
        },
        {
            "name": "Double Under Escape",
            "topPlayer": "Double under pass, maintain grip throughout",
            "bottomPlayer": "Break grips or create space to escape",
            "coaching": "Grip fighting under pressure",
            "skills": "#doubleunder #grips #escape"
        },
        {
            "name": "Compass Pass Game",
            "topPlayer": "Can only advance by passing in cardinal directions: N, S, E, W",
            "bottomPlayer": "Track direction changes and maintain guard",
            "coaching": "Directional control and awareness",
            "skills": "#angles #awareness #direction"
        }
    ],
    "Guard Retention": [
        {
            "name": "Frame Survival Game",
            "topPlayer": "Remove all frames within 20 seconds to pass",
            "bottomPlayer": "Maintain at least one frame on opponent",
            "coaching": "Frames are your shield",
            "skills": "#frames #structure #defense"
        },
        {
            "name": "Hip Escape Chain",
            "topPlayer": "Pressure forward to pass",
            "bottomPlayer": "Chain 3 hip escapes before recovering full guard",
            "coaching": "Continuous movement creates space",
            "skills": "#hipEscape #movement #space"
        },
        {
            "name": "Grip Strip Battle",
            "topPlayer": "Establish passing grips and maintain",
            "bottomPlayer": "Strip grips within 10 seconds or give up position",
            "coaching": "Fight at the grips first",
            "skills": "#grips #fighting #control"
        },
        {
            "name": "Distance Management",
            "topPlayer": "Close distance to pass",
            "bottomPlayer": "Use feet to maintain 2-foot distance for 20 seconds",
            "coaching": "Feet control distance",
            "skills": "#distance #feet #control"
        },
        {
            "name": "Shin Shield Hold",
            "topPlayer": "Remove shin shield and pass",
            "bottomPlayer": "Maintain shin shield contact for 15 seconds",
            "coaching": "Shield position is crucial",
            "skills": "#shinShield #halfGuard #retention"
        },
        {
            "name": "Inversion Recovery",
            "topPlayer": "Pass while bottom inverts",
            "bottomPlayer": "Use inversion to recover guard 3 times",
            "coaching": "Inversion creates angles",
            "skills": "#inversion #recovery #angles"
        },
        {
            "name": "Butterfly Hook Game",
            "topPlayer": "Remove both butterfly hooks to pass",
            "bottomPlayer": "Maintain at least one hook at all times",
            "coaching": "Hooks provide leverage",
            "skills": "#butterflyGuard #hooks #leverage"
        },
        {
            "name": "De La Riva Retention",
            "topPlayer": "Strip DLR hook and pass",
            "bottomPlayer": "Maintain DLR hook and control",
            "coaching": "Hook and grip work together",
            "skills": "#delariva #hook #control"
        },
        {
            "name": "Collar Sleeve Sweep or Retain",
            "topPlayer": "Pass the guard",
            "bottomPlayer": "Sweep or retain guard, can't let pass happen",
            "coaching": "Attack from guard retention",
            "skills": "#retention #sweeps #offense"
        },
        {
            "name": "Granby Roll Escape",
            "topPlayer": "Prevent granby roll escapes",
            "bottomPlayer": "Use granby rolls to recover guard from bad positions",
            "coaching": "Roll to create space",
            "skills": "#granby #escape #rolling"
        },
        {
            "name": "Two-on-One Grip Fight",
            "topPlayer": "Break two-on-one grip and pass",
            "bottomPlayer": "Maintain two-on-one grip for 15 seconds",
            "coaching": "Double team the arm",
            "skills": "#grips #twoonone #control"
        },
        {
            "name": "K-Guard Retention",
            "topPlayer": "Pass reverse De La Riva/K-guard",
            "bottomPlayer": "Maintain reverse DLR hook and off-balance opponent",
            "coaching": "Outside hook creates instability",
            "skills": "#reverseDLR #kguard #hooks"
        },
        {
            "name": "X-Guard Hold Challenge",
            "topPlayer": "Break X-guard hooks within 20 seconds",
            "bottomPlayer": "Maintain X-guard structure and off-balance",
            "coaching": "Two hooks control base",
            "skills": "#xguard #hooks #base"
        },
        {
            "name": "Open Guard Circuit",
            "topPlayer": "Apply passing pressure",
            "bottomPlayer": "Switch between 3 different open guards every 15 seconds",
            "coaching": "Variety creates problems",
            "skills": "#openGuard #variation #adaptation"
        },
        {
            "name": "Seated Guard Retention",
            "topPlayer": "Force opponent flat and pass",
            "bottomPlayer": "Maintain seated position and active feet",
            "coaching": "Stay active, never flat",
            "skills": "#seatedGuard #posture #activity"
        }
    ],
    "Half Guard": [
        {
            "name": "Underhook Battle",
            "topPlayer": "Establish overhook and flatten opponent",
            "bottomPlayer": "Fight for underhook and come to knees",
            "coaching": "Underhook wins the position",
            "skills": "#underhook #battle #halfguard"
        },
        {
            "name": "Knee Shield Maintenance",
            "topPlayer": "Remove knee shield and pass",
            "bottomPlayer": "Maintain knee shield for 20 seconds",
            "coaching": "Shield creates space and options",
            "skills": "#kneeShield #frames #space"
        },
        {
            "name": "Lockdown Control",
            "topPlayer": "Break lockdown and pass",
            "bottomPlayer": "Establish lockdown and sweep or take back",
            "coaching": "Lockdown controls the leg",
            "skills": "#lockdown #control #sweeps"
        },
        {
            "name": "Old School Sweep Setup",
            "topPlayer": "Prevent sweep and maintain base",
            "bottomPlayer": "Set up old school sweep or come to knees",
            "coaching": "Control the far leg",
            "skills": "#oldschool #sweep #halfguard"
        },
        {
            "name": "Deep Half Recovery",
            "topPlayer": "Prevent deep half entry and pass",
            "bottomPlayer": "Get to deep half guard position",
            "coaching": "Get underneath for recovery",
            "skills": "#deepHalf #recovery #position"
        },
        {
            "name": "Z-Guard Sweep Game",
            "topPlayer": "Pass Z-guard/knee shield",
            "bottomPlayer": "Sweep or come to knees from Z-guard",
            "coaching": "Shield and sweep together",
            "skills": "#zguard #sweeps #kneeShield"
        },
        {
            "name": "Crossface Escape",
            "topPlayer": "Establish crossface and flatten",
            "bottomPlayer": "Escape crossface and recover guard or sweep",
            "coaching": "Head control is critical",
            "skills": "#crossface #escape #head"
        },
        {
            "name": "Homer Simpson Sweep",
            "topPlayer": "Maintain base and prevent sweep",
            "bottomPlayer": "Off-balance and sweep using far leg",
            "coaching": "Attack the far leg",
            "skills": "#homer #sweep #offbalance"
        },
        {
            "name": "Coyote Guard Attack",
            "topPlayer": "Control leg and pass",
            "bottomPlayer": "Use coyote guard to attack back or sweep",
            "coaching": "Wrap the leg for control",
            "skills": "#coyote #back #attack"
        },
        {
            "name": "Quarter Guard Escape",
            "topPlayer": "Maintain quarter guard and advance",
            "bottomPlayer": "Recover full half guard or escape",
            "coaching": "Don't let them settle",
            "skills": "#quarterGuard #escape #recovery"
        },
        {
            "name": "Kimura from Half",
            "topPlayer": "Defend kimura and pass",
            "bottomPlayer": "Attack kimura from half guard",
            "coaching": "Submission or sweep from attack",
            "skills": "#kimura #halfguard #submission"
        },
        {
            "name": "93 Guard Series",
            "topPlayer": "Prevent back take",
            "bottomPlayer": "Use 93 guard to take back or sweep",
            "coaching": "Control head and shoulder",
            "skills": "#93guard #back #control"
        },
        {
            "name": "Half Butterfly Sweep",
            "topPlayer": "Remove butterfly hook and pass",
            "bottomPlayer": "Maintain half butterfly and sweep",
            "coaching": "Hook creates lift",
            "skills": "#halfButterfly #hook #sweep"
        },
        {
            "name": "Electric Chair Setup",
            "topPlayer": "Prevent lockdown and pass",
            "bottomPlayer": "Lockdown and attack electric chair",
            "coaching": "Lockdown to submission",
            "skills": "#electricchair #lockdown #submission"
        },
        {
            "name": "Half Guard Scramble",
            "topPlayer": "Advance position in scramble",
            "bottomPlayer": "Come up or take back in scramble",
            "coaching": "Stay mobile and aggressive",
            "skills": "#scramble #mobility #aggression"
        }
    ],
    "Top Control": [
        {
            "name": "Side Control Escape Timer",
            "topPlayer": "Maintain side control for 30 seconds",
            "bottomPlayer": "Escape to guard within 30 seconds",
            "coaching": "Weight distribution is key",
            "skills": "#sideControl #pressure #escape"
        },
        {
            "name": "Crossface Maintenance",
            "topPlayer": "Maintain crossface control entire round",
            "bottomPlayer": "Remove crossface and face opponent",
            "coaching": "Control the head to control the body",
            "skills": "#crossface #headControl #control"
        },
        {
            "name": "Knee on Belly Pressure",
            "topPlayer": "Maintain knee on belly for 20 seconds",
            "bottomPlayer": "Trap knee or escape to guard",
            "coaching": "Balance vs bucking",
            "skills": "#kneeOnBelly #pressure #balance"
        },
        {
            "name": "North-South Submission Hunt",
            "topPlayer": "Maintain north-south and attack submissions",
            "bottomPlayer": "Prevent subs and escape to guard",
            "coaching": "Heavy chest, active hands",
            "skills": "#northSouth #submissions #pressure"
        },
        {
            "name": "Gift Wrap Control",
            "topPlayer": "Establish gift wrap and maintain 15 seconds",
            "bottomPlayer": "Free arm and escape",
            "coaching": "Trap the arm to control",
            "skills": "#giftwrap #armControl #position"
        },
        {
            "name": "Scarfhold Escape Challenge",
            "topPlayer": "Maintain scarfhold position",
            "bottomPlayer": "Escape to guard or reverse",
            "coaching": "Head and arm control",
            "skills": "#scarfhold #kesa #control"
        },
        {
            "name": "Transitional Control",
            "topPlayer": "Flow between side, KOB, and north-south",
            "bottomPlayer": "Escape during transitions",
            "coaching": "Catch them between positions",
            "skills": "#transitions #flow #timing"
        },
        {
            "name": "Modified Scarfhold Attack",
            "topPlayer": "Modified scarf, attack near arm submissions",
            "bottomPlayer": "Protect arm and escape",
            "coaching": "Kimura, americana opportunities",
            "skills": "#modifiedScarf #armAttacks #control"
        },
        {
            "name": "100 Kilos Pressure",
            "topPlayer": "Make yourself as heavy as possible in side control",
            "bottomPlayer": "Create frames and breathing space",
            "coaching": "Distribute weight strategically",
            "skills": "#pressure #weight #heaviness"
        },
        {
            "name": "Twister Side Control",
            "topPlayer": "Twister side control, attack far leg",
            "bottomPlayer": "Prevent leg control and escape",
            "coaching": "Control the far side",
            "skills": "#twisterSide #legControl #unique"
        },
        {
            "name": "Reverse Scarf Spin",
            "topPlayer": "Reverse scarf, spin to submissions",
            "bottomPlayer": "Counter spin and escape",
            "coaching": "Movement creates submissions",
            "skills": "#reverseScarf #spinning #submissions"
        },
        {
            "name": "Shoulder Pressure Pin",
            "topPlayer": "Drive shoulder into face from side control",
            "bottomPlayer": "Create angle to escape shoulder pressure",
            "coaching": "Uncomfortable pressure creates mistakes",
            "skills": "#shoulderPressure #discomfort #control"
        },
        {
            "name": "Paper Cutter Setup",
            "topPlayer": "Set up paper cutter choke from side",
            "bottomPlayer": "Defend neck and escape",
            "coaching": "Collar grip to choke",
            "skills": "#papercutter #choke #setup"
        },
        {
            "name": "KOB to Mount Transition",
            "topPlayer": "KOB to mount transition when they react",
            "bottomPlayer": "Prevent mount by controlling knee",
            "coaching": "React to their reaction",
            "skills": "#kobToMount #transition #reading"
        },
        {
            "name": "Side Control Submission Chain",
            "topPlayer": "Attempt 3 different submissions from side",
            "bottomPlayer": "Defend all and escape",
            "coaching": "Chain attacks together",
            "skills": "#sideControl #chains #submissions"
        }
    ],
    "Mount": [
        {
            "name": "High Mount Maintenance",
            "topPlayer": "Climb to high mount and maintain 20 seconds",
            "bottomPlayer": "Prevent high mount or escape",
            "coaching": "Grapevine vs bridge",
            "skills": "#highMount #control #grapevine"
        },
        {
            "name": "S-Mount Attack",
            "topPlayer": "Establish S-mount and attack arm",
            "bottomPlayer": "Trap leg and escape",
            "coaching": "S-mount creates armbar angles",
            "skills": "#smount #armbar #position"
        },
        {
            "name": "Technical Mount Hold",
            "topPlayer": "Maintain technical mount for 15 seconds",
            "bottomPlayer": "Recover full guard",
            "coaching": "Hook and control head",
            "skills": "#technicalMount #hooks #control"
        },
        {
            "name": "Gift Wrap to Submission",
            "topPlayer": "Gift wrap from mount, attack chokes",
            "bottomPlayer": "Free arm and escape mount",
            "coaching": "Trap arm, attack neck",
            "skills": "#giftwrap #mount #chokes"
        },
        {
            "name": "Mount Escape Challenge",
            "topPlayer": "Maintain mount against all escapes",
            "bottomPlayer": "Try 3 different escape methods",
            "coaching": "Base vs technique",
            "skills": "#mountEscape #variety #technique"
        },
        {
            "name": "Low Mount Control",
            "topPlayer": "Maintain low mount and prevent escapes",
            "bottomPlayer": "Hip escape or bridge to recover guard",
            "coaching": "Low mount is easier to escape",
            "skills": "#lowMount #control #escape"
        },
        {
            "name": "Mounted Arm Triangle",
            "topPlayer": "Setup arm triangle from mount",
            "bottomPlayer": "Defend neck and escape mount",
            "coaching": "Head and arm position",
            "skills": "#armTriangle #mount #choke"
        },
        {
            "name": "Grapevine to Armbar",
            "topPlayer": "Grapevine legs, transition to armbar",
            "bottomPlayer": "Prevent grapevine and escape",
            "coaching": "Control hips to control body",
            "skills": "#grapevine #armbar #transition"
        },
        {
            "name": "Mounted Triangle Setup",
            "topPlayer": "Attack mounted triangle",
            "bottomPlayer": "Posture and stack to defend",
            "coaching": "Legs over shoulder to choke",
            "skills": "#mountedTriangle #choke #defense"
        },
        {
            "name": "Americana from Mount",
            "topPlayer": "Attack americana when arms extended",
            "bottomPlayer": "Keep elbows tight and escape",
            "coaching": "Extended arms are vulnerable",
            "skills": "#americana #keylock #mount"
        },
        {
            "name": "Thumb Choke Hunt",
            "topPlayer": "Search for thumb choke from mount",
            "bottomPlayer": "Defend throat and escape",
            "coaching": "Pressure based choke",
            "skills": "#thumbChoke #ezekiel #mount"
        },
        {
            "name": "Mount Transition Game",
            "topPlayer": "Switch between low, high, S, and technical mount",
            "bottomPlayer": "Escape during any transition",
            "coaching": "Variety prevents escape",
            "skills": "#mountVariation #transitions #control"
        },
        {
            "name": "Head and Arm Choke",
            "topPlayer": "Setup head and arm choke from mount",
            "bottomPlayer": "Defend by controlling elbow",
            "coaching": "Trap the arm deep",
            "skills": "#headandarm #darc #anaconda"
        },
        {
            "name": "Knee on Stomach Series",
            "topPlayer": "Mount to KOB to mount",
            "bottomPlayer": "Escape during transition",
            "coaching": "Pressure and movement",
            "skills": "#mountToKOB #transitions #pressure"
        },
        {
            "name": "Reverse Mount Control",
            "topPlayer": "Maintain reverse mount position",
            "bottomPlayer": "Roll through or escape",
            "coaching": "Unusual position, unusual opportunities",
            "skills": "#reverseMount #unique #control"
        }
    ],
    "Back Control": [
        {
            "name": "Seatbelt Maintenance",
            "topPlayer": "Maintain seatbelt control for 30 seconds",
            "bottomPlayer": "Strip grips and escape",
            "coaching": "Seatbelt controls the back",
            "skills": "#seatbelt #backControl #grips"
        },
        {
            "name": "Hook Retention Battle",
            "topPlayer": "Maintain both hooks in",
            "bottomPlayer": "Remove hooks and face opponent",
            "coaching": "Hooks prevent escape",
            "skills": "#hooks #retention #backControl"
        },
        {
            "name": "Rear Naked Choke Setup",
            "topPlayer": "Setup RNC, can reset if defended",
            "bottomPlayer": "Defend neck and escape",
            "coaching": "Hand fighting at the neck",
            "skills": "#RNC #choke #defense"
        },
        {
            "name": "Body Triangle Control",
            "topPlayer": "Establish body triangle and maintain",
            "bottomPlayer": "Break body triangle or escape",
            "coaching": "Triangle secures the position",
            "skills": "#bodyTriangle #control #backControl"
        },
        {
            "name": "Crucifix Position Hunt",
            "topPlayer": "Trap arm and get to crucifix",
            "bottomPlayer": "Protect arms and escape back",
            "coaching": "Crucifix immobilizes arms",
            "skills": "#crucifix #armTrap #control"
        },
        {
            "name": "Back Escape Hierarchy",
            "topPlayer": "Maintain back control",
            "bottomPlayer": "Use 3 escape methods progressively",
            "coaching": "Multiple escape paths",
            "skills": "#backEscape #hierarchy #system"
        },
        {
            "name": "Single Hook Back Take",
            "topPlayer": "Maintain single hook and establish second",
            "bottomPlayer": "Clear hook before second one enters",
            "coaching": "Don't give the second hook",
            "skills": "#singleHook #backTake #defense"
        },
        {
            "name": "Short Choke Attack",
            "topPlayer": "Attack short choke from back",
            "bottomPlayer": "Hide neck and escape",
            "coaching": "Gi or no-gi short choke",
            "skills": "#shortChoke #backAttack #choke"
        },
        {
            "name": "Bow and Arrow Setup",
            "topPlayer": "Setup bow and arrow choke",
            "bottomPlayer": "Prevent grip and escape",
            "coaching": "Control collar and leg",
            "skills": "#bowandArrow #choke #setup"
        },
        {
            "name": "Armbar from Back",
            "topPlayer": "Transition to armbar from back",
            "bottomPlayer": "Defend arm and escape",
            "coaching": "When neck fails, take arm",
            "skills": "#armbar #backControl #transition"
        },
        {
            "name": "Clock Choke Hunt",
            "topPlayer": "Set up clock choke from back",
            "bottomPlayer": "Defend and escape to guard",
            "coaching": "Roll to finish choke",
            "skills": "#clockChoke #choke #rolling"
        },
        {
            "name": "Twister Hookm Control",
            "topPlayer": "Get twister hook from back",
            "bottomPlayer": "Clear leg and escape",
            "coaching": "Leg control from the back",
            "skills": "#twister #legControl #back"
        },
        {
            "name": "Rear Triangle Setup",
            "topPlayer": "Attack triangle from back",
            "bottomPlayer": "Posture and escape",
            "coaching": "Legs over shoulder from behind",
            "skills": "#rearTriangle #triangle #back"
        },
        {
            "name": "Harness Grip Battle",
            "topPlayer": "Establish harness grip and maintain",
            "bottomPlayer": "Strip harness and escape",
            "coaching": "Alternative to seatbelt",
            "skills": "#harness #grips #back"
        },
        {
            "name": "Hooks vs Feet on Hips",
            "topPlayer": "Keep hooks in",
            "bottomPlayer": "Get feet on hips to create space",
            "coaching": "Battle for hip control",
            "skills": "#hooks #hips #control"
        }
    ],
    "Front Headlock": [
        {
            "name": "Front Headlock Control Hold",
            "topPlayer": "Maintain front headlock for 20 seconds",
            "bottomPlayer": "Hand fight and clear head",
            "coaching": "Head position is everything",
            "skills": "#frontHeadlock #control #head"
        },
        {
            "name": "Darce Choke Setup",
            "topPlayer": "Setup darce from front headlock",
            "bottomPlayer": "Defend arm position and posture",
            "coaching": "Arm in, head controlled",
            "skills": "#darce #choke #armIn"
        },
        {
            "name": "Anaconda Hunt",
            "topPlayer": "Attack anaconda choke",
            "bottomPlayer": "Keep arm out and posture",
            "coaching": "Opposite of darce positioning",
            "skills": "#anaconda #choke #frontHeadlock"
        },
        {
            "name": "Guillotine Transition",
            "topPlayer": "Front headlock to guillotine",
            "bottomPlayer": "Defend neck and posture out",
            "coaching": "Guard pull with guillotine",
            "skills": "#guillotine #transition #choke"
        },
        {
            "name": "Japanese Necktie Setup",
            "topPlayer": "Attack Japanese necktie",
            "bottomPlayer": "Roll through and escape",
            "coaching": "Unique angle on choke",
            "skills": "#japaneseNecktie #choke #unique"
        },
        {
            "name": "Front Headlock to Back",
            "topPlayer": "Take back from front headlock",
            "bottomPlayer": "Prevent back take, return to guard",
            "coaching": "Swing to the back",
            "skills": "#frontToBack #transition #backTake"
        },
        {
            "name": "Crank vs Choke",
            "topPlayer": "Apply front headlock pressure",
            "bottomPlayer": "Defend and escape within 15 seconds",
            "coaching": "Control the spine",
            "skills": "#crank #pressure #frontHeadlock"
        },
        {
            "name": "Arm-In Guillotine",
            "topPlayer": "Attack arm-in guillotine",
            "bottomPlayer": "Defend by keeping head low",
            "coaching": "High elbow finish",
            "skills": "#armInGuillotine #choke #defense"
        },
        {
            "name": "Front Headlock Scramble",
            "topPlayer": "Maintain front headlock through scramble",
            "bottomPlayer": "Escape head and come up",
            "coaching": "Stay calm in chaos",
            "skills": "#scramble #frontHeadlock #chaos"
        },
        {
            "name": "Snap Down Series",
            "topPlayer": "Snap down and control",
            "bottomPlayer": "Sprawl and come back up",
            "coaching": "Control the head, control the match",
            "skills": "#snapDown #control #wrestling"
        },
        {
            "name": "North-South Choke Transition",
            "topPlayer": "Front headlock to north-south choke",
            "bottomPlayer": "Defend transition and escape",
            "coaching": "Roll to finish",
            "skills": "#northSouthChoke #transition #choke"
        },
        {
            "name": "Peruvian Necktie",
            "topPlayer": "Setup Peruvian necktie",
            "bottomPlayer": "Clear legs and escape",
            "coaching": "Rare but effective",
            "skills": "#peruvianNecktie #choke #rare"
        },
        {
            "name": "Front Headlock Knee Tap",
            "topPlayer": "Front headlock to knee tap takedown",
            "bottomPlayer": "Base out and sprawl",
            "coaching": "Off-balance and finish",
            "skills": "#kneeTap #takedown #frontHeadlock"
        },
        {
            "name": "High Wrist Control",
            "topPlayer": "Control high wrist from front headlock",
            "bottomPlayer": "Strip wrist control and escape",
            "coaching": "Wrist control immobilizes",
            "skills": "#wristControl #frontHeadlock #immobilize"
        },
        {
            "name": "Double Attack Series",
            "topPlayer": "Alternate between darce and anaconda",
            "bottomPlayer": "Defend both and escape",
            "coaching": "One leads to the other",
            "skills": "#doubleAttack #darce #anaconda"
        }
    ],
    "Turtle": [
        {
            "name": "Turtle Breakdown Challenge",
            "topPlayer": "Break turtle down to side control",
            "bottomPlayer": "Maintain turtle or return to guard",
            "coaching": "Stay tight and mobile",
            "skills": "#turtle #breakdown #defense"
        },
        {
            "name": "Clock Choke from Turtle",
            "topPlayer": "Setup clock choke",
            "bottomPlayer": "Counter roll and escape",
            "coaching": "Roll with the choke",
            "skills": "#clockChoke #turtle #rolling"
        },
        {
            "name": "Back Take from Turtle",
            "topPlayer": "Take back with hooks from turtle",
            "bottomPlayer": "Defend hooks and return to guard",
            "coaching": "Don't give both hooks",
            "skills": "#backTake #turtle #hooks"
        },
        {
            "name": "Turtle Escape Game",
            "topPlayer": "Control turtle and prevent escape",
            "bottomPlayer": "Escape to guard or standing within 20 seconds",
            "coaching": "Forward or reverse roll",
            "skills": "#turtleEscape #movement #timing"
        },
        {
            "name": "Seatbelt from Turtle",
            "topPlayer": "Establish seatbelt grip from turtle",
            "bottomPlayer": "Strip grips before they settle",
            "coaching": "Fight grips immediately",
            "skills": "#seatbelt #turtle #grips"
        },
        {
            "name": "Crucifix from Turtle",
            "topPlayer": "Trap arm and get crucifix",
            "bottomPlayer": "Keep arms safe and escape",
            "coaching": "Protect arms in turtle",
            "skills": "#crucifix #turtle #armTrap"
        },
        {
            "name": "Twister from Turtle",
            "topPlayer": "Setup twister position",
            "bottomPlayer": "Clear leg control and escape",
            "coaching": "Leg control to submission",
            "skills": "#twister #turtle #submission"
        },
        {
            "name": "Spiral Ride Control",
            "topPlayer": "Use spiral ride to break turtle",
            "bottomPlayer": "Counter spiral and stand up",
            "coaching": "Wrestling control applied to BJJ",
            "skills": "#spiralRide #wrestling #turtle"
        },
        {
            "name": "Granby Roll Counter",
            "topPlayer": "Counter granby roll attempts",
            "bottomPlayer": "Use granby to escape turtle",
            "coaching": "Roll with control",
            "skills": "#granby #turtle #counter"
        },
        {
            "name": "Peterson Roll",
            "topPlayer": "Maintain control",
            "bottomPlayer": "Use Peterson roll to reverse",
            "coaching": "Wrestling reversal from turtle",
            "skills": "#petersonRoll #reversal #wrestling"
        },
        {
            "name": "Sit Out Escape",
            "topPlayer": "Prevent sit out",
            "bottomPlayer": "Sit out and face opponent",
            "coaching": "Wrestling escape to BJJ",
            "skills": "#sitOut #escape #wrestling"
        },
        {
            "name": "Turtle Guard Attack",
            "topPlayer": "Pass turtle guard",
            "bottomPlayer": "Use turtle as active position, sweep or submit",
            "coaching": "Turtle as offensive position",
            "skills": "#turtleGuard #offense #unique"
        },
        {
            "name": "Near Leg Ride",
            "topPlayer": "Control near leg from turtle",
            "bottomPlayer": "Clear leg and escape",
            "coaching": "Leg control immobilizes",
            "skills": "#nearLeg #control #turtle"
        },
        {
            "name": "Truck Position Entry",
            "topPlayer": "Get to truck from turtle",
            "bottomPlayer": "Prevent leg control",
            "coaching": "Unconventional back attack",
            "skills": "#truck #turtle #position"
        },
        {
            "name": "Straight Jacket Control",
            "topPlayer": "Trap both arms from turtle",
            "bottomPlayer": "Free arms and escape",
            "coaching": "Immobilize before attacking",
            "skills": "#straightJacket #armControl #turtle"
        }
    ],
    "Escapes": [
        {
            "name": "Bridge and Shrimp Drill",
            "topPlayer": "Maintain side control",
            "bottomPlayer": "Alternate bridge and shrimp to escape",
            "coaching": "Fundamental escape movements",
            "skills": "#bridge #shrimp #fundamentals"
        },
        {
            "name": "Elbow Escape Series",
            "topPlayer": "Keep opponent flat",
            "bottomPlayer": "Chain elbow escapes to recover guard",
            "coaching": "Persistent shrimping",
            "skills": "#elbowEscape #shrimp #guard"
        },
        {
            "name": "Frame Escape Challenge",
            "topPlayer": "Remove frames and maintain",
            "bottomPlayer": "Use frames to create escape space",
            "coaching": "Frames create structure",
            "skills": "#frames #escape #structure"
        },
        {
            "name": "Trap and Roll Escape",
            "topPlayer": "Maintain mount",
            "bottomPlayer": "Trap arm and leg, bridge to escape",
            "coaching": "Classic mount escape",
            "skills": "#trapAndRoll #mountEscape #bridge"
        },
        {
            "name": "Granby Roll Escape Drill",
            "topPlayer": "Control opponent",
            "bottomPlayer": "Use granby rolls to escape bad positions",
            "coaching": "Inverted escape movements",
            "skills": "#granby #escape #inversion"
        },
        {
            "name": "Ghost Escape Practice",
            "topPlayer": "Maintain side control",
            "bottomPlayer": "Use ghost escape to recover guard",
            "coaching": "Modern escape technique",
            "skills": "#ghost #escape #modern"
        },
        {
            "name": "Running Man Escape",
            "topPlayer": "Maintain mount",
            "bottomPlayer": "Running man escape to guard",
            "coaching": "Active hips and feet",
            "skills": "#runningMan #mountEscape #hips"
        },
        {
            "name": "Back Escape Progression",
            "topPlayer": "Maintain back control",
            "bottomPlayer": "Progress through escape hierarchy",
            "coaching": "Systematic back escape",
            "skills": "#backEscape #progression #system"
        },
        {
            "name": "Seated Guard Recovery",
            "topPlayer": "Prevent guard recovery",
            "bottomPlayer": "Come to seated guard from bad position",
            "coaching": "Active recovery to seated",
            "skills": "#seatedGuard #recovery #escape"
        },
        {
            "name": "KOB Escape Options",
            "topPlayer": "Maintain knee on belly",
            "bottomPlayer": "Try 3 different KOB escapes",
            "coaching": "Multiple escape paths",
            "skills": "#KOBescape #options #variety"
        },
        {
            "name": "Crossface Escape Method",
            "topPlayer": "Maintain crossface",
            "bottomPlayer": "Remove crossface and face opponent",
            "coaching": "Answer the crossface first",
            "skills": "#crossface #escape #facing"
        },
        {
            "name": "North-South Escape",
            "topPlayer": "Maintain north-south",
            "bottomPlayer": "Bridge and turn to escape",
            "coaching": "Timing the bridge",
            "skills": "#northSouth #escape #timing"
        },
        {
            "name": "Scarfhold Reversal",
            "topPlayer": "Maintain scarfhold",
            "bottomPlayer": "Reverse to top position",
            "coaching": "Power through the reversal",
            "skills": "#scarfhold #reversal #power"
        },
        {
            "name": "Technical Stand Up",
            "topPlayer": "Take opponent down",
            "bottomPlayer": "Use technical stand up to get up",
            "coaching": "Safe stand up method",
            "skills": "#technicalStandUp #escape #standing"
        },
        {
            "name": "Inversion Escape",
            "topPlayer": "Control opponent",
            "bottomPlayer": "Invert to escape and recover",
            "coaching": "Upside down escape",
            "skills": "#inversion #escape #recovery"
        }
    ],
    "Submissions": [
        {
            "name": "Armbar from Guard Setup",
            "topPlayer": "Defend armbar and maintain posture",
            "bottomPlayer": "Setup and finish armbar from guard",
            "coaching": "Control the arm fully",
            "skills": "#armbar #guard #submission"
        },
        {
            "name": "Triangle Choke Progression",
            "topPlayer": "Posture and defend triangle",
            "bottomPlayer": "Setup triangle step by step",
            "coaching": "Angle and squeeze",
            "skills": "#triangle #choke #progression"
        },
        {
            "name": "Kimura from Everywhere",
            "topPlayer": "Defend kimura",
            "bottomPlayer": "Attack kimura from multiple positions",
            "coaching": "Kimura is everywhere",
            "skills": "#kimura #submission #versatile"
        },
        {
            "name": "Straight Ankle Lock Battle",
            "topPlayer": "Apply straight ankle lock",
            "bottomPlayer": "Defend and counter",
            "coaching": "Control the heel",
            "skills": "#anklelock #leglock #defense"
        },
        {
            "name": "Rear Naked Choke Finish",
            "topPlayer": "Finish RNC from back",
            "bottomPlayer": "Defend neck and escape",
            "coaching": "Squeeze don't pull",
            "skills": "#RNC #choke #back"
        },
        {
            "name": "Guillotine Variations",
            "topPlayer": "Defend guillotine",
            "bottomPlayer": "Attack different guillotine variations",
            "coaching": "High elbow vs arm-in",
            "skills": "#guillotine #variations #choke"
        },
        {
            "name": "Omoplata Setup Game",
            "topPlayer": "Defend and roll through",
            "bottomPlayer": "Setup omoplata from guard",
            "coaching": "Trap the shoulder",
            "skills": "#omoplata #shoulder #submission"
        },
        {
            "name": "Heel Hook Entries",
            "topPlayer": "Defend leg and extract",
            "bottomPlayer": "Enter heel hook position safely",
            "coaching": "Control before attacking",
            "skills": "#heelhook #leglock #entry"
        },
        {
            "name": "Arm Triangle Hunt",
            "topPlayer": "Setup arm triangle from top",
            "bottomPlayer": "Defend and escape",
            "coaching": "Head and arm position",
            "skills": "#armTriangle #choke #top"
        },
        {
            "name": "Wrist Lock Opportunities",
            "topPlayer": "Defend wrists",
            "bottomPlayer": "Attack wrist locks throughout match",
            "coaching": "Opportunistic attacks",
            "skills": "#wristlock #opportunistic #submission"
        },
        {
            "name": "Kneebar from Top",
            "topPlayer": "Attack kneebar from passing",
            "bottomPlayer": "Defend and recover guard",
            "coaching": "Leg attack while passing",
            "skills": "#kneebar #passing #leglock"
        },
        {
            "name": "Ezekiel Choke Series",
            "topPlayer": "Attack ezekiel from multiple positions",
            "bottomPlayer": "Defend throat and escape",
            "coaching": "Sleeve or no sleeve",
            "skills": "#ezekiel #choke #versatile"
        },
        {
            "name": "Baseball Choke Setup",
            "topPlayer": "Setup baseball choke",
            "bottomPlayer": "Strip grips and escape",
            "coaching": "Lapel grip position",
            "skills": "#baseball #choke #grips"
        },
        {
            "name": "D'Arce from Scramble",
            "topPlayer": "Catch darce during scramble",
            "bottomPlayer": "Defend arm-in position",
            "coaching": "Opportunistic in chaos",
            "skills": "#darce #scramble #opportunistic"
        },
        {
            "name": "Submission Chain Game",
            "topPlayer": "Chain 3 submissions together",
            "bottomPlayer": "Defend all without giving position",
            "coaching": "Flow between attacks",
            "skills": "#chains #flow #multiple"
        }
    ],
    "Leg Locks": [
        {
            "name": "Ashi Garami Entry",
            "topPlayer": "Enter ashi garami position",
            "bottomPlayer": "Defend leg and extract",
            "coaching": "Control before attacking",
            "skills": "#ashiGarami #entry #control"
        },
        {
            "name": "50/50 Position Battle",
            "topPlayer": "Attack from 50/50",
            "bottomPlayer": "Defend and counter attack",
            "coaching": "Whoever attacks first wins",
            "skills": "#5050 #leglock #battle"
        },
        {
            "name": "Heel Hook Finish Game",
            "topPlayer": "Finish heel hook (controlled)",
            "bottomPlayer": "Defend and extract safely",
            "coaching": "Slow and controlled",
            "skills": "#heelhook #finish #control"
        },
        {
            "name": "Outside Ashi Entry",
            "topPlayer": "Enter outside ashi position",
            "bottomPlayer": "Counter and extract",
            "coaching": "Outside control angle",
            "skills": "#outsideAshi #entry #leglock"
        },
        {
            "name": "Inside Sankaku Entry",
            "topPlayer": "Enter inside sankaku",
            "bottomPlayer": "Defend and escape",
            "coaching": "Inside position control",
            "skills": "#insideSankaku #entry #leglock"
        },
        {
            "name": "Saddle Position Hunt",
            "topPlayer": "Get to saddle/4-11 position",
            "bottomPlayer": "Prevent saddle entry",
            "coaching": "Highest control position",
            "skills": "#saddle #411 #control"
        },
        {
            "name": "Kneebar from Guard",
            "topPlayer": "Attack kneebar from guard",
            "bottomPlayer": "Defend and pass",
            "coaching": "Straight leg attack",
            "skills": "#kneebar #guard #straight"
        },
        {
            "name": "Toe Hold Opportunities",
            "topPlayer": "Setup toe hold throughout match",
            "bottomPlayer": "Protect foot position",
            "coaching": "Ankle and foot rotation",
            "skills": "#toehold #ankle #rotation"
        },
        {
            "name": "Calf Slicer Setup",
            "topPlayer": "Attack calf slicer",
            "bottomPlayer": "Extend leg to defend",
            "coaching": "Compression lock",
            "skills": "#calfSlicer #compression #leglock"
        },
        {
            "name": "Estima Lock Game",
            "topPlayer": "Setup Estima lock from top",
            "bottomPlayer": "Defend ankle and escape",
            "coaching": "Ankle compression",
            "skills": "#estimaLock #ankle #compression"
        },
        {
            "name": "K-Guard to Leg Lock",
            "topPlayer": "Attack legs from K-guard",
            "bottomPlayer": "Defend and pass",
            "coaching": "Reverse DLR to leg attacks",
            "skills": "#kguard #legAttack #entry"
        },
        {
            "name": "X-Guard Kneebar Entry",
            "topPlayer": "Attack kneebar from X-guard",
            "bottomPlayer": "Defend and extract",
            "coaching": "X position to leg lock",
            "skills": "#xguard #kneebar #entry"
        },
        {
            "name": "SLX Entry Game",
            "topPlayer": "Enter single leg X for leg attacks",
            "bottomPlayer": "Block entry and pass",
            "coaching": "SLX position control",
            "skills": "#SLX #entry #control"
        },
        {
            "name": "Leg Lock Defense Drill",
            "topPlayer": "Attack different leg locks",
            "bottomPlayer": "Defend and extract from each",
            "coaching": "Know your leg lock escapes",
            "skills": "#legDefense #escapes #knowledge"
        },
        {
            "name": "Leg Entanglement Flow",
            "topPlayer": "Flow between leg entanglement positions",
            "bottomPlayer": "Prevent transitions",
            "coaching": "Position before submission",
            "skills": "#entanglement #flow #transitions"
        }
    ],
    "Takedowns": [
        {
            "name": "Double Leg Finish",
            "topPlayer": "Setup and finish double leg",
            "bottomPlayer": "Sprawl and defend",
            "coaching": "Level change and penetration",
            "skills": "#doubleLeg #wrestling #takedown"
        },
        {
            "name": "Single Leg Series",
            "topPlayer": "Attack single leg, finish with variation",
            "bottomPlayer": "Defend and counter",
            "coaching": "Multiple single leg finishes",
            "skills": "#singleLeg #wrestling #finishes"
        },
        {
            "name": "Ankle Pick Setup",
            "topPlayer": "Setup ankle pick takedown",
            "bottomPlayer": "Defend and sprawl",
            "coaching": "Off-balancing entry",
            "skills": "#anklePick #offbalance #takedown"
        },
        {
            "name": "Arm Drag to Back",
            "topPlayer": "Arm drag to back take",
            "bottomPlayer": "Counter drag and face",
            "coaching": "Drag and circle",
            "skills": "#armDrag #back #takedown"
        },
        {
            "name": "Body Lock Takedown",
            "topPlayer": "Establish body lock and take down",
            "bottomPlayer": "Hand fight and defend",
            "coaching": "Control the body",
            "skills": "#bodyLock #control #takedown"
        },
        {
            "name": "Snap Down Game",
            "topPlayer": "Snap opponent down to turtle",
            "bottomPlayer": "Sprawl and return to standing",
            "coaching": "Control the head",
            "skills": "#snapDown #headControl #takedown"
        },
        {
            "name": "Low Single Attack",
            "topPlayer": "Attack low single leg",
            "bottomPlayer": "Wizard defense",
            "coaching": "Low penetration step",
            "skills": "#lowSingle #wrestling #takedown"
        },
        {
            "name": "Fireman's Carry",
            "topPlayer": "Setup fireman's carry throw",
            "bottomPlayer": "Defend and sprawl",
            "coaching": "Under and lift",
            "skills": "#firemansCarry #throw #takedown"
        },
        {
            "name": "Duck Under Series",
            "topPlayer": "Duck under to back or takedown",
            "bottomPlayer": "Prevent duck under",
            "coaching": "Level change under arm",
            "skills": "#duckUnder #level #back"
        },
        {
            "name": "Foot Sweep Setup",
            "topPlayer": "Setup and execute foot sweep",
            "bottomPlayer": "Base and defend",
            "coaching": "Timing and balance",
            "skills": "#footSweep #timing #judo"
        },
        {
            "name": "Front Headlock to Mat",
            "topPlayer": "Front headlock to mat return",
            "bottomPlayer": "Defend and stand up",
            "coaching": "Control head to control body",
            "skills": "#frontHeadlock #matReturn #wrestling"
        },
        {
            "name": "Hip Toss Entry",
            "topPlayer": "Setup hip toss",
            "bottomPlayer": "Block hip and defend",
            "coaching": "Hip positioning crucial",
            "skills": "#hipToss #judo #throw"
        },
        {
            "name": "Guard Pull Counter",
            "topPlayer": "Counter opponent's guard pull",
            "bottomPlayer": "Successfully pull guard",
            "coaching": "Timing the counter",
            "skills": "#guardPull #counter #timing"
        },
        {
            "name": "Knee Tap Finish",
            "topPlayer": "Setup knee tap takedown",
            "bottomPlayer": "Base out and defend",
            "coaching": "Off-balance and tap",
            "skills": "#kneeTap #offbalance #takedown"
        },
        {
            "name": "High Crotch Attack",
            "topPlayer": "Attack high crotch takedown",
            "bottomPlayer": "Crossface and defend",
            "coaching": "Head positioning critical",
            "skills": "#highCrotch #wrestling #head"
        }
    ],
    "Transitions": [
        {
            "name": "Guard to Mount Flow",
            "topPlayer": "Transition from guard to mount",
            "bottomPlayer": "Prevent transitions",
            "coaching": "Connect positions smoothly",
            "skills": "#guardToMount #transition #flow"
        },
        {
            "name": "Side to Mount Transition",
            "topPlayer": "Move from side control to mount",
            "bottomPlayer": "Block knee and prevent mount",
            "coaching": "Knee slide to mount",
            "skills": "#sideToMount #transition #knee"
        },
        {
            "name": "Mount to Back Take",
            "topPlayer": "Transition from mount to back",
            "bottomPlayer": "Defend back take",
            "coaching": "Follow the turn",
            "skills": "#mountToBack #transition #back"
        },
        {
            "name": "Turtle to Back Flow",
            "topPlayer": "Turtle to back take",
            "bottomPlayer": "Prevent hooks and escape",
            "coaching": "Hook insertion timing",
            "skills": "#turtleToBack #hooks #timing"
        },
        {
            "name": "KOB to Submission",
            "topPlayer": "KOB to submission attempt",
            "bottomPlayer": "Defend and escape",
            "coaching": "Pressure to attack",
            "skills": "#KOBtoSub #pressure #submission"
        },
        {
            "name": "Guard Pass to Submission",
            "topPlayer": "Pass directly to submission",
            "bottomPlayer": "Defend during transition",
            "coaching": "Chaining pass and attack",
            "skills": "#passToSub #chain #attack"
        },
        {
            "name": "Scramble Advantage",
            "topPlayer": "Win scrambles to better position",
            "bottomPlayer": "Win scrambles to guard",
            "coaching": "Movement and timing",
            "skills": "#scramble #movement #advantage"
        },
        {
            "name": "Standing to Ground Flow",
            "topPlayer": "Takedown directly to submission position",
            "bottomPlayer": "Defend transition",
            "coaching": "Connect standing and ground",
            "skills": "#standToGround #flow #connection"
        },
        {
            "name": "Sweep to Submission",
            "topPlayer": "Sweep directly to submission",
            "bottomPlayer": "Defend during reversal",
            "coaching": "Capitalize on reversals",
            "skills": "#sweepToSub #reversal #submission"
        },
        {
            "name": "Failed Pass Recovery",
            "topPlayer": "Recover when pass fails",
            "bottomPlayer": "Capitalize on failed pass",
            "coaching": "Don't give up position",
            "skills": "#recovery #resilience #defense"
        },
        {
            "name": "Back to Mount Switch",
            "topPlayer": "Switch from back to mount",
            "bottomPlayer": "Escape during transition",
            "coaching": "Read the escape",
            "skills": "#backToMount #reading #switch"
        },
        {
            "name": "North-South to Side",
            "topPlayer": "Flow between north-south and side",
            "bottomPlayer": "Escape during movement",
            "coaching": "Constant movement",
            "skills": "#NStoSide #flow #control"
        },
        {
            "name": "Leg Lock to Pass",
            "topPlayer": "Failed leg lock to pass",
            "bottomPlayer": "Defend and retain",
            "coaching": "Transition from legs",
            "skills": "#legToPass #transition #adaptation"
        },
        {
            "name": "Guard Recovery Chain",
            "topPlayer": "Prevent guard recovery",
            "bottomPlayer": "Chain recovery attempts",
            "coaching": "Multiple paths to guard",
            "skills": "#recovery #chain #guard"
        },
        {
            "name": "Position Before Submission",
            "topPlayer": "Advance position before attacking",
            "bottomPlayer": "Prevent positional advances",
            "coaching": "Hierarchy of control",
            "skills": "#positionFirst #hierarchy #control"
        }
    ]
}

def generate_games():
    """Generate 200 NoGi grappling games across 13 topics"""
    games = []
    base_timestamp = int(datetime.now().timestamp() * 1000)
    game_id = base_timestamp

    # Calculate games per topic (approximately 15 each to reach ~200)
    games_per_topic = 15

    for topic in TOPICS:
        templates = GAME_TEMPLATES[topic]
        game_number = 1

        # Use all 15 templates for each topic
        for i, template in enumerate(templates):
            game = {
                "id": game_id,
                "name": template["name"],
                "topic": topic,
                "gameNumber": str(game_number),
                "topPlayer": template["topPlayer"],
                "bottomPlayer": template["bottomPlayer"],
                "coaching": template["coaching"],
                "skills": template["skills"],
                "favorite": False,
                "lastUsed": None,
                "created": base_timestamp + i
            }
            games.append(game)
            game_id += 1
            game_number += 1

    return games

def main():
    print("Generating 200 NoGi grappling games...")
    games = generate_games()

    # Create output
    output = {
        "games": games,
        "metadata": {
            "totalGames": len(games),
            "totalTopics": len(TOPICS),
            "topics": TOPICS,
            "generated": datetime.now().isoformat(),
            "description": "NoGi grappling games library using constraint-led approach principles"
        }
    }

    # Save to JSON file
    with open('/home/user/roa/nogi-games-library.json', 'w') as f:
        json.dump(output, f, indent=2)

    print(f"✓ Generated {len(games)} games across {len(TOPICS)} topics")
    print(f"✓ Saved to: nogi-games-library.json")

    # Print summary
    print("\n=== Summary ===")
    for topic in TOPICS:
        count = len([g for g in games if g['topic'] == topic])
        print(f"{topic}: {count} games")
    print(f"\nTotal: {len(games)} games")

if __name__ == "__main__":
    main()
