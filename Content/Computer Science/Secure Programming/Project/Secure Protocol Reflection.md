## Standardised Protocol

- even before coming up with a protocol, we found the entire idea quite ambitious. 200 people with varying experience and ambition agreeing on something as complicated as a messaging protocol will be very difficult
- did it work in the end? for the most part yes, we got a working agreed upon protocol. However, like with most things in life, the majority if it's implementation was implemented by a small group of the cohort, rather than everyone. I think it would be naiive to expect every single person to have some input, but I feel like we should have had a better way to get input from a variety of people, rather than just the ones who took the assignment head on - give a suggestion of things here.
- As for the protocol itself, I mostly have no issues with it. I do feel as though the message structures are bloated, could be more barebones.
- for example, there only needs to be 1 hello message, regardless of client or server. The recipient should be able to tell who it came from depending on the address. To achieve this, we would need stricter compliance in terms of deployment; i.e. a client and server must be hosted on the same device. Only 1 server can represent and IP address. This would improve security by reducing things like authenticity, and integrity (explain this more) and also simply message structure. 
- moreover, the protocol documentation was quite vague in places. There could definitely be more work done to explain integration between messages. Ie - server sends hello, then client asks for update, then server sends update, etc. Things like this would reduce confusion and improve interoperability
- I also felt like there were was a major issue in terms of broadcast storms that should have been dealt with protocol side, rather than implementation side. More specifically, when a server recieve a public message, it forwards this message to every other server. Then those servers forward it to every other server. To fix it, the servers would need to split the message apart and individually send messages to each other server. This puts a lot of strain on the sending server, which IMO defeats the purpose of a mesh network. All of this could be fixed by adding a simple from: field in the message structure to stop broadcast storms.
- but for the most part, the protocol worked! It was absolutely incredible to test our implementation against other implementations in a psuedo black box (each side only knows their own code) and actually be able to send protected messages over the internet. That is a feeling I will remember for the rest of my life. 

## Design Choices
- Decided to write the protocol implementation entirely in python, with a react frontend.
- Deployed using vite + docker. Flask powers frontend communication with the backend.
	- Docker was a really big part of our implementation and personally I think it makes it stand out from the rest.
	- It allowed us to dynamically set options in our deployments - message retention, ports, ip addresses, etc. I think our implementation could work straight out of the box and be deployed as its currently implemented. 
	- Every other implementation I reviewed had some kind of a device issue that didn't outline a specific library or dependancy that needed to be installed first. Docker fixes all of these issues.
- Just used the langauges I was most comfortable with. I would like to have delved into Rust / Go for this assignment just to get some experience with them, but ultimately did not have enough time and didn't want to burden other group members with an unfamiliar language.
- Tried to be as modular as possible - creating shared utilities such as message structure and crypto compliance so that they can be unit tested, rather than only through integration
- Used TDD. Tests determine protocol / security compliance for shared libraries before I even began implementing the actual skeleton of the client / server architecture. 
- As spoken about in the previous section, a huge issue we faced during implementation were public chat broadcast storms. Since we needed to strictly comply with the protocol and not add extra fields, we needed to come up with a clever way to only forward messages once. To fix this, we made sending servers split public messages into seperate messages, with one intended recipient each. This way, when a receiving server got a message, it wouldn't try to forward it other servers and create a broadcast storm.
- The actual implementation can run completely headless (without the react frontend), so theoretically anyone can interact with a client via it's API layer. This is a tradeoff I made - security vs functionality (flask api vs websockets) to reduce the complexity of frontend communication. While it's still protocol compliant and for the most part safe, it can still potentially be the weakest link in terms of security. 

### Demonstration
- For demonstration purposes, I will go over the *real* deployment steps, not the testing steps (which include premade compose files and setup scripts to make marking easier).
- All of this is outlined in detail in the code's readme (link to appendix).
- Deployment is really easy, user just needs to setup their client / server compose files as they want - ip addresses, ports, message retention etc.
	- In retrospect, this process could be made more user friendly but doing this requires actual testing and more time than we had. 
	- Clients / servers could be integrated into a single module so that user's have less settings to deal with.
	- Users not familiar with docker / compose might have a difficult time to get it running - although this did not seem to be a problem for peer reviews.
- After the compose files are setup, users just need to create the client containers and they have full access to the application (reword this please)

