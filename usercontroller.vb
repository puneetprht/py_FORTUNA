<Route("user/sendpasswordresetlink")>
        <HttpGet>
        Public Function SendPasswordResetLink(ByVal e As String, ByVal resetGuid As String) As HttpResponseMessage
            Dim objUserApp As New UserApp()
            Dim user As Models.UserModel = objUserApp.GetUserByEmail(e)

            If Not user Is Nothing Then
                If Not objUserApp.SendPasswordResetEmail(user.PmuserEx.Email, user.PmuserEx.ObjFirstName & " " & user.PmuserEx.ObjLastName, resetGuid) Then
                    Return _response.Error(Request, "Error occurred.")
                End If
                Return _response.OK(Request)
            End If

            Return _response.Error(Request, "User not found")
        End Function