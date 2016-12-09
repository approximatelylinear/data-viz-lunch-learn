
# coding: utf-8

# # How Does Babby Data?

# ## Overview
# 
# What it says on the tin ^^^ .
# 
# 
# ### Data Ops
# 
# Ensures data storage, integrity and processing capacity
# 
# ### Data Transformation
# 
# Converts data from one form to another. Examples are: 
# 
# 1. Normalization ("I lIke PupPies!!" -> "i like puppies")
# 2. Lexical Analysis ("i like puppies" -> ["i", "like", "puppies"])
# 3. Aggregation (["i", "like", "puppies"] -> 3)
# 4. Application of statistical models (["i", "like", "puppies"] -> "interest:animals")
# 
# ### Reporting
# 
# Presents summarized information about the data in a system. These summarizations could be:
# 
# 1. Numeric
# 2. Text-based
# 3. Visual
# 
# #### Ad Hoc
# 
# Oh hey! Real quick, could you tell me this thing about the data that you've never provided to me before? Or maybe you've given it to me before, but you have to calculate it by hand each time?
# 
# #### Automated
# 
# Let ROBOT DATA answer just this one question over and over and over each and every day with just slightly new parameters.
# 
# ----
# 
# ----

# ## Types of Systems

# ### Transactional
# 
# * Powers real-time experiences that require little knowledge of past state. 
# * Requires fast inserts and fast responses to simple queries.
# 
# 
# #### Coupon redemption at point-of-sale
# You've signed up for Jellyvision's newest made-up app _ALEX-Me-Now_. Go you! Marketers can tell Jellyvision to send you a coupon for a free ALEX counseling session whenever you walk into your local convenience store. But ... how could it work? 
# 
# ##### Coupon Generation
# 1. The app monitors your location and sends a stream of location events to an event queue up in CloudLand
# 2. The `Are-They-In-a-Store?` processor subscribes to this queue
#     * The processor publishes events to the `Coupon Database` every time a user enters a relevant store
# 3. A `Notify-them!` processor subscribes to changes to the `Coupon Database` and pushes a notification to the app 
# 
# ##### Coupon Redemption
# 1. A user selects the new coupon in the _ALEX-Me-Now_ interface and gets directed to ALEX 
# 2. ALEX validates coupon using the `Coupon Database` and let's them into the app!
# 
# ##### Interlude
# Ashley: Hey! A lot of users are using the same coupon multiple times. We gotta fix this!
# 
# Sydney: Oh, right. I bet we could just delete the row after they've redeemed it. That would solve the problem!
# 
# Ashley: Perfect!
# 
# ----

# ### Analytical
# 
# * Powers complex analytical tasks that examine at large and disparate portions of data. 
# * Requires fast responses to complicated queries along arbitrary dimensions
# 
# #### Analyzing coupon redemption at point-of-sale
# _ALEX-Me-Now_ is a huge hit!! The servers are blowing up, so it's *gotta* be working. Now the execs want to improve it's usage in the largest markets. But, they just have to know...
# 
# * How many ALEX coupons have been redeemed exactly? 
# * Where do users actually redeem the most ALEX coupons? 
# 
# ##### Interlude
# Ashley: Hey Jordan, can you look at the data and tell us where people have been redeeming coupons and how many?
# 
# Jordan: Um... You never recorded and/or just deleted that data. So, no?
# 
# Ashley: Do it anyway pp kthxbye. Oh! I forgot to mention: stop querying our system because it is slowing down the user experience down. Ok, bye for real!
# 
# ----
# 
# So... wait up. Are you as depressed as me now?
# 
# * Is this saying the demands on a successful transactional system and a successful analytical system are different? 
# 
# * Is this doomed to be a loveless partnership? 
# 
# * Will they never reconcile their differences?
# 
# ----
# 
# ----

# ## Principals of Love and War in Data
# 
# ### (1) History must be recorded or it never happened
# * At every **point in time** we need to know the **state of the world**.
# * We need to write down this state of the world either *directly* or *indirectly*
# * That state must be true for all time!
# * We must be able to say: What we have recorded _is_ the world. Anyone who asserts anything different is simply misinformed.
# 
# ### (2) Hoomans are stoopid
# * We're always forgetting stuff!
# * We only consider our own context. 
# * We are _super_ good at convincing ourselves we understand the implications of a system, when we really, um, don't. 
# * But, in those cases where our silly heuristics work -- We are GENIUSES
# 
# ### (3) State is written in STONE. *STONE*. 
# * Keep a source-of-record. This source of record _is_ the world, and not just a representation of it.
# * Do not store pointers to things that might change in the source of record.
# * Never modify data directly, only modify copies
# * Destruction of data is only done when the data _has_ to disappear for ethical or legal reasons, never application convenience
# 
# ### (4) State should be both recoverable and discoverable
# * Rolling back the world to a particular state should be both possible, easy and frequently done. 
# * You should always be able to quickly find what you need. Each element of the world state should be indexed and retrievable. Optimize for (2): You will never know all of your analytics queries ahead of time, but you will always be able to run them
# 
# ----
# 
# ----

# 
# ## Putting it together: Lambda Architecture
# 
# Across a hot desert, two mountain ranges and one small sea, there is a land called DATA. Inside this land is the Queen-who-Talks-a-lot-I-mean-A-LOT (QwTalImaL) and a library (ALEXandria) where a band of scribes records her every word and deed in the holy materials of stone and wax. 
# 
# ### Master dataset
# 
# The stone tablets of the Scribes of ALEXandria. (There's a huge cavern full of them out back.)
# 
# ### Speed layer
# 
# Every day at dawn, the current Stone Tablet is copied onto wax tablets. Scribes record very recent pronouncements and deeds onto these wax tablets.
# 
# 
# ### Serving layer
# 
# Anyone who wants to learn of the great works of QwTalImaL may read the Wax Tablets in the suite of special reading rooms that are managed by an expert set of Curators. Ask to know of any pronouncement or deed and you will be given all the wax tablets that pertain. If you should need to look very far back, there is a smaller set of older guides who know the Stone Tablets, and will present copies of those to you as well. They're kinda slow though...
# 
# 
# ### Batch layer
# 
# Nightly stone carvers laboriously copy over the current Wax Tablet to a new Stone Tablet and then very carefully store the old Stone Tablet. These tablets will all remain in the universe post-heat-death, because good data never fades (except for legal or ethical reasons) and the queen is pretty insistent about people knowing and loving her. 
# 
# ----
# 
# ----

# ## Putting it together: _ALEX-Me-Now_
# 
# Cool story, bro, but weren't we talking about some coupon app or something?
# 
# ok. FINE. Let's try to update Ashley and Sydney's strategy for the happiness of everyone. 
# 
# ##### Coupon Generation
# 1. The app monitors your location and sends a stream of location events to an event queue up in CloudLand
#     * [NEW!] Define the State-of-the-World:
#         * User ID
#         * Location
#             * Geographic coordinates
#             * Country, State, City
#         * Timestamp
# 
# 2. The `Are-They-In-a-Store?` processor subscribes to this queue
#     * [NEW!] The processor publishes events to the `Coupon Redemtion Database` every time a user enters a relevant store
#     * [NEW!] The processor publishes State-of-the-World events to the `Coupon History Database` every time a user enters a relevant store
#         * User ID
#         * Location
#         * Store
#         * Timestamp
# 3. A `Notify-them!` processor subscribes to changes to the `Coupon Database` and pushes a notification to the app 
# 
# ##### Coupon Redemption
# 1. A user selects the new coupon in the _ALEX-Me-Now_ interface and gets directed to ALEX 
# 2. ALEX validates coupon using the `Coupon Database` and let's them into the app!
# 4. [NEW!] Validation events are pushed to the `ALEX History Database`
# 
# ##### Coupon Analysis
# 
# Discuss!!
