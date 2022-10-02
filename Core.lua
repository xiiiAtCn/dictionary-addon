Dictionary = LibStub("AceAddon-3.0"):NewAddon("Dictionary", "AceConsole-3.0", "AceEvent-3.0")

function Dictionary:OnInitialize()
-- Called when the addon is loaded
  self:Print("dictionary has inited")
-- register chat commands
  self:RegisterChatCommand("dic", "SlashCommand")
  self:RegisterChatCommand("dictionary", "SlashCommand")
-- load dictionary file
  DictionaryMap = DictionaryMap or {}
  self:merge()
end

function Dictionary:OnEnable()
-- Called when the addon is enabled
  self:RegisterEvent("ZONE_CHANGED")
end

function Dictionary:OnDisable()
  -- Called when the addon is disabled
end

function Dictionary:ZONE_CHANGED()
  local subzone = GetSubZoneText()
  self:Print("Current Place", subzone)
  self:Print("You have changed zones!", GetZoneText(), subzone)
  if GetBindLocation() == subzone then
    self:Print("Welcome Home!")
  end
end

function Dictionary:SlashCommand(msg) 
  if msg then
    local explaination = DictionaryMap[msg]
    if explaination == nil then
      self:Print("cannot find word in dictionary, cache \"", msg,  "\" in dictionary. Wait to search after quit game.")
    DictionaryMap[msg] = ""
    else
      self:Print(msg, " means: ", explaination)
    end
  else
    self:Print("You mast input words")
  end
end

-- merge dictionary
function Dictionary:merge()
  for k, v in pairs(DefaultDictionary) do
    DictionaryMap[k] = v
  end
end