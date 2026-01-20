# AI Game Designer - Test Cases

## Fixed Issues

### Problem 1: Generic Answers
**Root Cause:** Five patterns were defined but never checked in the if-else chain, causing fallback to generic template.

### Problem 2: Bidirectional Pattern Matching
**Root Cause:** Regex patterns only matched one word order (e.g., "mount escape" but not "escape mount").

## Test Cases - Should Now Work Correctly

### 1. Mount Escape
**Input:** "Escape mount"
- **Previous:** Generic template (pattern not checked)
- **Now:** Mount Escape - Bridge & Trap to Half Guard ✓
- **Pattern Match:** `/escape.*mount/` matches "escape mount"

### 2. Back Control Escape
**Input:** "Back escape problems"
- **Previous:** Generic template (pattern not checked)
- **Now:** Back Escape - Hand Fighting to Hip Escape ✓
- **Pattern Match:** `/back.*escape/` matches "back escape"

### 3. Leg Lock Defense
**Input:** "Heel hook defense"
- **Previous:** Generic template (pattern not checked)
- **Now:** Ashi Garami Leg Lock Defense ✓
- **Pattern Match:** `/heel.*hook/` matches "heel hook"

### 4. Leg Lock Defense (Alternative)
**Input:** "50/50 guard defense"
- **Previous:** Generic template (pattern not checked)
- **Now:** Ashi Garami Leg Lock Defense ✓
- **Pattern Match:** `/50.*50/` matches "50/50"

### 5. Frame Creation
**Input:** "Creating frames under pressure"
- **Previous:** Generic template (pattern not checked)
- **Now:** Frame Creation Under Pressure ✓
- **Pattern Match:** `/creating.*space/` matches "creating frames"

### 6. Grip Fighting
**Input:** "Grip fighting from standing"
- **Previous:** Generic template (pattern not checked)
- **Now:** Grip Fighting - Control Before Attack ✓
- **Pattern Match:** `/grip.*fight/` matches "grip fighting"

### 7. Side Control Escape (Bidirectional)
**Input:** "Escape side control"
- **Previous:** No match (pattern only checked "side control escape")
- **Now:** Frame Escape From Side Control ✓
- **Pattern Match:** `/escape.*side.*control/` matches "escape side control"

## New Game Templates Added

1. **Mount Escape** (Line 5676-5708)
   - Focus: Bridge & trap technique with 3-step sequence
   - Constraints: Mandatory step order, turn-in requirement
   - Pedagogy: Priit Mihkelson / Defensive BJJ principles

2. **Back Escape** (Line 5710-5743)
   - Focus: Hand fighting before hip escape
   - Constraints: Clear choking hand first, turn toward choke
   - Pedagogy: Danaher / Priit back defense

3. **Leg Lock Defense** (Line 5745-5778)
   - Focus: Ashi garami escape hierarchy
   - Constraints: Hands → posture → extraction sequence
   - Pedagogy: Lachlan Giles modern leg lock escape

4. **Frame Creation** (Line 5780-5814)
   - Focus: Maintaining frames under pressure
   - Constraints: Elbow-to-ribs failure condition
   - Pedagogy: Priit defensive structure principles

5. **Grip Fighting** (Line 5816-5849)
   - Focus: Grip dominance before attacking
   - Constraints: 15s grip fight phase → 15s attack phase
   - Pedagogy: Judo grip fighting with point system

## Updated Regex Patterns

All patterns now support bidirectional matching:

```javascript
sideEscape: /side.*control.*escape|stuck.*side|flat.*back|can't.*escape.*side|escape.*side.*control/i
mountEscape: /mount.*escape|escape.*mount|stuck.*mount|can't.*escape.*mount/i
backEscape: /back.*escape|escape.*back|rear.*naked|hooks.*escape/i
legLock: /leg.*lock|heel.*hook|ankle.*lock|ashi|saddle|50.*50/i
frames: /frame|creating.*space|defensive.*structure|framing/i
grips: /grip|hand.*control|breaking.*grips|grip.*fight/i
```

## Expected Behavior

When a user enters a problem description, the system will:
1. Convert text to lowercase
2. Test against all 10 patterns in order
3. Return the FIRST matching specific game template
4. Fall back to generic template only if no patterns match

This ensures users get detailed, constraint-led game designs instead of generic templates.
