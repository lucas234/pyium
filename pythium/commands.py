

class Commands:
    """
    driver.execute_script('mobile: Commands', )
    the below commands are supported(Android and iOS)
    """
    Scroll = "scroll"
    GetContexts = "getContexts"
    ViewportScreenshot = "viewportScreenshot"
    ViewportRect = "viewportRect"
    StartLogsBroadcast = "startLogsBroadcast"
    StopLogsBroadcast = "stopLogsBroadcast"
    BatteryInfo = "batteryInfo"
    DeviceInfo = "deviceInfo"
    GetDeviceTime = "getDeviceTime"
    DeleteFile = "deleteFile"


class AndroidCommands(Commands):
    """
    driver.execute_script('mobile: Commands', )
    the below commands are supported(only Android)
    """
    Shell = "shell"
    ExecEmuConsoleCommand = "execEmuConsoleCommand"
    DragGesture = "dragGesture"
    FlingGesture = "flingGesture"
    DoubleClickGesture = "doubleClickGesture"
    LongClickGesture = "longClickGesture"
    PinchCloseGesture = "pinchCloseGesture"
    PinchOpenGesture = "pinchOpenGesture"
    SwipeGesture = "swipeGesture"
    ScrollGesture = "scrollGesture"
    ScrollBackTo = "scrollBackTo"
    DeepLink = "deepLink"
    AcceptAlert = "acceptAlert"
    DismissAlert = "dismissAlert"
    ChangePermissions = "changePermissions"
    GetPermissions = "getPermissions"
    PerformEditorAction = "performEditorAction"
    StartScreenStreaming = "startScreenStreaming"
    StopScreenStreaming = "stopScreenStreaming"
    GetNotifications = "getNotifications"
    ListSms = "listSms"
    Type = "type"
    SensorSet = "sensorSet"
    ClearApp = "clearApp"
    StartActivity = "startActivity"
    StartService = "startService"
    StopService = "stopService"
    Broadcast = "broadcast"
    InstallMultipleApks = "installMultipleApks"


class IosCommands(Commands):
    """
    driver.execute_script('mobile: Commands', )
    the below commands are supported (only iOS)
    """
    Tap = "tap"
    SelectPickerWheelValue = "selectPickerWheelValue"
    Swipe = "swipe"
    Pinch = "pinch"
    DoubleTap = "doubleTap"
    TwoFingerTap = "twoFingerTap"
    TapWithNumberOfTaps = "tapWithNumberOfTaps"
    TouchAndHold = "touchAndHold"
    DragFromToForDuration = "dragFromToForDuration"
    RotateElement = "rotateElement"
    Alert = "alert"
    SetPasteboard = "setPasteboard"
    GetPasteboard = "getPasteboard"
    Source = "source"
    InstallApp = "installApp"
    IsAppInstalled = "isAppInstalled"
    RemoveApp = "removeApp"
    LaunchApp = "launchApp"
    TerminateApp = "terminateApp"
    QueryAppState = "queryAppState"
    ActivateApp = "activateApp"
    StartPerfRecord = "startPerfRecord"
    StopPerfRecord = "stopPerfRecord"
    InstallCertificate = "installCertificate"
    ActiveAppInfo = "activeAppInfo"
    DeviceScreenInfo = "deviceScreenInfo"
    PressButton = "pressButton"
    EnrollBiometric = "enrollBiometric"
    SendBiometricMatch = "sendBiometricMatch"
    IsBiometricEnrolled = "isBiometricEnrolled"
    ClearKeychains = "clearKeychains"
    GetPermission = "getPermission"
    SetPermission = "setPermission"
    ResetPermission = "resetPermission"
    GetAppearance = "getAppearance"
    SetAppearance = "setAppearance"
    SiriCommand = "siriCommand"
    DeleteFolder = "deleteFolder"
    StartAudioRecording = "startAudioRecording"
    StopAudioRecording = "stopAudioRecording"
    RunXCTest = "runXCTest"
    InstallXCTestBundle = "installXCTestBundle"
    ListXCTestBundles = "listXCTestBundles"
    ListXCTestsInTestBundle = "listXCTestsInTestBundle"
    PushNotification = "pushNotification"
    ExpectNotification = "expectNotification"
    PerformIoHidEvent = "performIoHidEvent"
    ConfigureLocalization = "configureLocalization"
    ResetLocationService = "resetLocationService"

