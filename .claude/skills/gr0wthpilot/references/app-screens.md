# App screens: real ones only

The Founder's rule: show only the Product's real screens, from its own recorded test screenshots, topped up by building the app and driving it in the simulator for missing shots and the walkthrough recording.
No screen the Product does not have is ever shown, and no real screen's content is altered.
Framing a real screenshot (a device frame, a caption, a crop) is fine; drawing UI that is not there is not.

## 1. Use the recorded evidence first

Many Products keep screenshots from their own UI tests and reviews.
Immerse, for example, keeps several hundred PNGs under `Evidence/` (visual sweeps, asset reviews, the native app's screens).
List them with `find <repo>/Evidence -name '*.png'`, pick by what each shows, and copy the ones you use into the package (`02-brand/screens/`, `04-video/screens/`, or where the deliverable lives).
Record each in `<package>/screens-manifest.md`:

```
| Package file | Source | Commit | What it shows |
| --- | --- | --- | --- |
| 04-video/screens/roll-counter.png | repo:Evidence/NativeApp/visual-sweep-048/roll-counter.png | 8eb6f50 | the 24-exposure counter mid-roll |
```

## 2. Build and drive the app for what is missing

Every simulator step goes through `gp-sim`, every build through `gp-xcodebuild`, each run as a single command (no pipes, chains, or redirections).

```
gp-xcodebuild source                          # a verified copy of the repo's committed tree in <build>/source/
gp-xcodebuild -project <copy>/App/Immerse/Immerse.xcodeproj -scheme Immerse \
  -destination 'generic/platform=iOS Simulator' build
gp-sim create                                 # Gr0wthPilot-<Product>-1, newest iPhone Pro, newest iOS
gp-sim boot <udid>
gp-sim status-bar <udid>                      # 9:41, full signal, full battery
gp-sim install <udid> <build>/DerivedData/Build/Products/Debug-iphonesimulator/Immerse.app
gp-sim launch <udid> <bundle id> [-- launch arguments the repo documents]
gp-sim screenshot <udid> <package>/04-video/screens/<name>.png
gp-sim record-start <udid> <package>/04-video/raw/walkthrough.mp4
gp-sim record-stop <udid>
gp-sim cleanup
```

`<build>` is the guard's build folder, which the preflight prints as `build`; no tool of the run can write it, which is why `gp-xcodebuild` builds there and `gp-sim` installs only from there.
The copy is checked against its commit before every build; give `-project`, `-workspace`, and `-xcconfig` paths inside it, name a test plan with `-testPlan <name>`, and leave DerivedData to the wrapper.
Read the Product's README and AGENTS.md for its build command, its test-only launch arguments (Immerse has a Debug testing unlock), and any simulator notes.
To move through screens for a recording, run the Product's own UI tests against the run's simulator (`gp-xcodebuild ... -destination 'platform=iOS Simulator,id=<udid>' test -only-testing:<a UI test>`) while recording, or relaunch with the launch arguments that open each screen.
Prefer a short sequence of real screens cut together with ffmpeg over a long unedited recording.

Keep the Mac usable: one booted simulator at a time, and `gp-sim cleanup` at the end of phase 3, at the end of the run, and after any failed simulator step.
`gp-sim` never touches a simulator the run did not create.

## 3. A Product that is not an iOS app

Use the same rule with that Product's own evidence: screenshots from its tests, or the web app served locally and captured with `gp-chrome screenshot`.
If no real screen can be captured, the video and the screenshots say so and use none; never mock one.
